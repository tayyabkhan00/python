import React, { useEffect, useRef, useState } from 'react';
import { Camera, Hand } from 'lucide-react';

const HandParticleSystem = () => {
  const containerRef = useRef(null);
  const [isTracking, setIsTracking] = useState(false);
  const [error, setError] = useState('');
  const sceneRef = useRef(null);
  const cameraRef = useRef(null);
  const rendererRef = useRef(null);
  const particlesRef = useRef(null);
  const handPositionRef = useRef({ x: 0, y: 0, z: 0 });
  const videoRef = useRef(null);
  const handsRef = useRef(null);
  const animationIdRef = useRef(null);

  useEffect(() => {
    if (!containerRef.current) return;

    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
    script.async = true;
    
    script.onload = () => {
      initThreeJS();
    };
    
    document.head.appendChild(script);

    return () => {
      if (animationIdRef.current) {
        cancelAnimationFrame(animationIdRef.current);
      }
      if (rendererRef.current) {
        if (containerRef.current && rendererRef.current.domElement && containerRef.current.contains(rendererRef.current.domElement)) {
          containerRef.current.removeChild(rendererRef.current.domElement);
        }
        rendererRef.current.dispose();
      }
      if (particlesRef.current) {
        particlesRef.current.geometry.dispose();
        particlesRef.current.particles.material.dispose();
      }
    };
  }, []);

  const initThreeJS = () => {
    if (!containerRef.current) return;

    const THREE = window.THREE;
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x0a0a0a);
    sceneRef.current = scene;

    const camera = new THREE.PerspectiveCamera(
      75,
      containerRef.current.clientWidth / containerRef.current.clientHeight,
      0.1,
      1000
    );
    camera.position.z = 50;
    cameraRef.current = camera;

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(containerRef.current.clientWidth, containerRef.current.clientHeight);
    containerRef.current.appendChild(renderer.domElement);
    rendererRef.current = renderer;

    const particleCount = 5000;
    const positions = new Float32Array(particleCount * 3);
    const velocities = new Float32Array(particleCount * 3);
    const colors = new Float32Array(particleCount * 3);

    for (let i = 0; i < particleCount * 3; i += 3) {
      positions[i] = (Math.random() - 0.5) * 100;
      positions[i + 1] = (Math.random() - 0.5) * 100;
      positions[i + 2] = (Math.random() - 0.5) * 100;

      velocities[i] = (Math.random() - 0.5) * 0.2;
      velocities[i + 1] = (Math.random() - 0.5) * 0.2;
      velocities[i + 2] = (Math.random() - 0.5) * 0.2;

      const color = new THREE.Color();
      color.setHSL(Math.random(), 0.8, 0.6);
      colors[i] = color.r;
      colors[i + 1] = color.g;
      colors[i + 2] = color.b;
    }

    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    const material = new THREE.PointsMaterial({
      size: 0.8,
      vertexColors: true,
      transparent: true,
      opacity: 0.8,
      blending: THREE.AdditiveBlending
    });

    const particles = new THREE.Points(geometry, material);
    scene.add(particles);
    particlesRef.current = { particles, velocities, geometry };

    const animate = () => {
      animationIdRef.current = requestAnimationFrame(animate);

      const positions = particlesRef.current.geometry.attributes.position.array;
      const velocities = particlesRef.current.velocities;
      const handPos = handPositionRef.current;

      for (let i = 0; i < positions.length; i += 3) {
        const dx = handPos.x - positions[i];
        const dy = handPos.y - positions[i + 1];
        const dz = handPos.z - positions[i + 2];
        const distance = Math.sqrt(dx * dx + dy * dy + dz * dz);

        if (distance < 30) {
          const force = (30 - distance) / 30;
          velocities[i] += dx * force * 0.01;
          velocities[i + 1] += dy * force * 0.01;
          velocities[i + 2] += dz * force * 0.01;
        }

        positions[i] += velocities[i];
        positions[i + 1] += velocities[i + 1];
        positions[i + 2] += velocities[i + 2];

        velocities[i] *= 0.98;
        velocities[i + 1] *= 0.98;
        velocities[i + 2] *= 0.98;

        if (Math.abs(positions[i]) > 50) velocities[i] *= -0.5;
        if (Math.abs(positions[i + 1]) > 50) velocities[i + 1] *= -0.5;
        if (Math.abs(positions[i + 2]) > 50) velocities[i + 2] *= -0.5;
      }

      particlesRef.current.geometry.attributes.position.needsUpdate = true;
      particlesRef.current.particles.rotation.y += 0.001;

      renderer.render(scene, camera);
    };
    animate();

    const handleResize = () => {
      if (!containerRef.current || !cameraRef.current || !rendererRef.current) return;
      cameraRef.current.aspect = containerRef.current.clientWidth / containerRef.current.clientHeight;
      cameraRef.current.updateProjectionMatrix();
      rendererRef.current.setSize(containerRef.current.clientWidth, containerRef.current.clientHeight);
    };
    window.addEventListener('resize', handleResize);
  };

  const startHandTracking = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      
      const video = document.createElement('video');
      video.srcObject = stream;
      video.play();
      videoRef.current = video;

      const script = document.createElement('script');
      script.src = 'https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js';
      document.head.appendChild(script);

      script.onload = () => {
        const hands = new window.Hands({
          locateFile: (file) => {
            return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
          }
        });

        hands.setOptions({
          maxNumHands: 1,
          modelComplexity: 1,
          minDetectionConfidence: 0.5,
          minTrackingConfidence: 0.5
        });

        hands.onResults((results) => {
          if (results.multiHandLandmarks && results.multiHandLandmarks.length > 0) {
            const hand = results.multiHandLandmarks[0];
            const indexTip = hand[8];
            
            handPositionRef.current = {
              x: (indexTip.x - 0.5) * 100,
              y: -(indexTip.y - 0.5) * 100,
              z: -indexTip.z * 50
            };
          }
        });

        handsRef.current = hands;

        const sendFrame = async () => {
          if (videoRef.current && videoRef.current.readyState === 4) {
            await hands.send({ image: videoRef.current });
          }
          if (isTracking) {
            requestAnimationFrame(sendFrame);
          }
        };
        sendFrame();
      };

      setIsTracking(true);
      setError('');
    } catch (err) {
      setError('Failed to access camera. Please allow camera permissions.');
      console.error(err);
    }
  };

  const stopHandTracking = () => {
    setIsTracking(false);
    if (videoRef.current && videoRef.current.srcObject) {
      videoRef.current.srcObject.getTracks().forEach(track => track.stop());
    }
    handPositionRef.current = { x: 0, y: 0, z: 0 };
  };

  return (
    <div className="w-full h-screen bg-black flex flex-col">
      <div className="absolute top-4 left-4 z-10 bg-black/70 backdrop-blur-sm p-4 rounded-lg border border-purple-500/30">
        <h1 className="text-2xl font-bold text-white mb-2 flex items-center gap-2">
          <Hand className="w-6 h-6 text-purple-400" />
          Hand-Controlled Particles
        </h1>
        <p className="text-gray-300 text-sm mb-3">
          Move your index finger to attract particles
        </p>
        <button
          onClick={isTracking ? stopHandTracking : startHandTracking}
          className={`flex items-center gap-2 px-4 py-2 rounded-lg font-semibold transition-all ${
            isTracking
              ? 'bg-red-500 hover:bg-red-600 text-white'
              : 'bg-purple-500 hover:bg-purple-600 text-white'
          }`}
        >
          <Camera className="w-4 h-4" />
          {isTracking ? 'Stop Tracking' : 'Start Hand Tracking'}
        </button>
        {error && (
          <p className="text-red-400 text-sm mt-2">{error}</p>
        )}
        {isTracking && (
          <div className="mt-3 flex items-center gap-2">
            <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
            <span className="text-green-400 text-sm">Tracking active</span>
          </div>
        )}
      </div>
      
      <div ref={containerRef} className="flex-1 w-full" />
      
      <div className="absolute bottom-4 right-4 bg-black/70 backdrop-blur-sm p-3 rounded-lg border border-purple-500/30 text-gray-300 text-sm">
        <p><strong className="text-purple-400">Tip:</strong> Point your index finger at the screen</p>
        <p className="mt-1">Particles will be attracted to your fingertip!</p>
      </div>
    </div>
  );
};

export default HandParticleSystem;
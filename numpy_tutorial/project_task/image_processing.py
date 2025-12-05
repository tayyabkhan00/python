import numpy as np

img = np.random.randint(0,255,(28,28))
img_norm = img / 255.0
img_flip = img[:, ::-1]
kernel = np.ones((3,3)) / 9

blurred = np.zeros_like(img, dtype=float)
for i in range(1,27):
    for j in range(1,27):
        region = img[i-1:i+2, j-1:j+2]
        blurred[i,j] = np.sum(region * kernel)

binary = (img_norm > 0.5).astype(int)

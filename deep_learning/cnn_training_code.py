import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# -----------------------------
# 1. Load CIFAR-10 Dataset
# -----------------------------
transform = transforms.Compose([
    transforms.ToTensor(),               # Convert image → tensor
    transforms.Normalize((0.5, 0.5, 0.5),
                         (0.5, 0.5, 0.5)) # Normalize pixels
])

train_set = torchvision.datasets.CIFAR10(root='./data', train=True,
                                         download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=32,
                                           shuffle=True)

test_set = torchvision.datasets.CIFAR10(root='./data', train=False,
                                        download=True, transform=transform)
test_loader = torch.utils.data.DataLoader(test_set, batch_size=32,
                                          shuffle=False)

# -----------------------------
# 2. Build CNN Model
# -----------------------------
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        
        # Convolution Layers
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)  # input=3 channels, output=32
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)

        # Pooling
        self.pool = nn.MaxPool2d(2, 2)

        # Fully connected layers
        self.fc1 = nn.Linear(64 * 8 * 8, 256)   # flatten → dense
        self.fc2 = nn.Linear(256, 10)           # 10 classes

        # Activation
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.conv1(x))   # Conv1 + ReLU
        x = self.pool(x)               # Downsample

        x = self.relu(self.conv2(x))   # Conv2 + ReLU
        x = self.pool(x)               # Downsample

        x = x.view(-1, 64 * 8 * 8)     # Flatten
        x = self.relu(self.fc1(x))     # Dense layer
        x = self.fc2(x)                # Output layer
        return x

model = SimpleCNN()

# -----------------------------
# 3. Loss & Optimizer
# -----------------------------
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# -----------------------------
# 4. Train the CNN
# -----------------------------
for epoch in range(5):  # Train for 5 epochs
    running_loss = 0.0
    
    for images, labels in train_loader:
        optimizer.zero_grad()         # Reset gradients
        outputs = model(images)       # Forward pass
        loss = criterion(outputs, labels)
        loss.backward()               # Backpropagation
        optimizer.step()              # Update weights
        
        running_loss += loss.item()
    
    print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader)}")

print("Training Completed 🎉")

# -----------------------------
# 5. Test Accuracy
# -----------------------------
correct = 0
total = 0
model.eval()

with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Accuracy: {100 * correct / total:.2f}%")

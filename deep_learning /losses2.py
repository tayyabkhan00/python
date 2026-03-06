import torch
import torch.nn as nn

# -----------------------------------------
# 1. MEAN SQUARED ERROR (MSE)
# -----------------------------------------

# true and predicted values
y_true_reg = torch.tensor([3.0, 3.0])
y_pred_reg = torch.tensor([4.0, 5.0])

# PyTorch MSE Loss
mse_loss = nn.MSELoss()
mse_output = mse_loss(y_pred_reg, y_true_reg)

print("MSE Loss:", mse_output.item())


# -----------------------------------------
# 2. BINARY CROSS ENTROPY (BCE)
# -----------------------------------------

# true and predicted values
y_true_bce = torch.tensor([1.0])     # actual: class = 1
y_pred_bce = torch.tensor([0.9])     # predicted probability

# PyTorch BCE Loss
bce_loss = nn.BCELoss()
bce_output = bce_loss(y_pred_bce, y_true_bce)

print("Binary Cross Entropy Loss:", bce_output.item())


# -----------------------------------------
# 3. CATEGORICAL CROSS ENTROPY (CCE)
# -----------------------------------------

# true class (0, 1, or 2)
y_true_class = torch.tensor([0])  # class index

# predicted probabilities (from softmax)
y_pred_probs = torch.tensor([[0.8, 0.15, 0.05]])  # 3 classes

# PyTorch Categorical Cross Entropy
cce_loss = nn.CrossEntropyLoss()
cce_output = cce_loss(y_pred_probs, y_true_class)   # NO one-hot needed

print("Categorical Cross Entropy Loss:", cce_output.item())


# ⭐ Version With Softmax + CCE (If you want probability input)
import torch
import torch.nn as nn
import torch.nn.functional as F

y_true_class = torch.tensor([0])
logits = torch.tensor([[2.1, 1.0, 0.1]])  # raw model output (logits)

# softmax to convert logits to probabilities
probs = F.softmax(logits, dim=1)
print("Softmax probabilities:", probs)

# CCE Loss
cce_loss = nn.CrossEntropyLoss()
loss = cce_loss(logits, y_true_class)

print("CCE Loss:", loss.item())

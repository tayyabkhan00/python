import torch
import torch.nn as nn

# --------------------------
# 1. MSE (Mean Squared Error)
# --------------------------

mse = nn.MSELoss()

y_true = torch.tensor([3.0])
y_pred = torch.tensor([4.0])

mse_loss = mse(y_pred, y_true)
print("MSE:", mse_loss.item())


# --------------------------
# 2. BCE (Binary Cross Entropy)
# --------------------------

bce = nn.BCELoss()

y_true = torch.tensor([1.0])      # actual class = 1
y_pred = torch.tensor([0.8])      # predicted probability

bce_loss = bce(y_pred, y_true)
print("BCE:", bce_loss.item())


# --------------------------
# 3. CCE (Categorical Cross Entropy)
# --------------------------

cce = nn.CrossEntropyLoss()

y_true = torch.tensor([0])        # correct class index = 0
y_pred = torch.tensor([[2.0, 1.0, 0.1]])   # logits for 3 classes

cce_loss = cce(y_pred, y_true)
print("CCE:", cce_loss.item())

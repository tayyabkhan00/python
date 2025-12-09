# Simple example: one neuron learning

x = 2             # input
y_true = 5        # actual output

w = 0.5           # weight
b = 1             # bias
lr = 0.01         # learning rate

# Forward pass
y_pred = w*x + b
loss = (y_pred - y_true)**2

# Compute gradients
d_loss_d_pred = 2 * (y_pred - y_true)
d_pred_d_w = x
d_pred_d_b = 1

# Backprop (update weights)
w = w - lr * d_loss_d_pred * d_pred_d_w
b = b - lr * d_loss_d_pred * d_pred_d_b

print("Updated weight:", w)
print("Updated bias:", b)

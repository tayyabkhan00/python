import torch
import torch.nn as nn

lstm = nn.LSTM(input_size=5, hidden_size=10, num_layers=1, batch_first=True)

x = torch.randn(1, 3, 5)   # batch=1, seq_len=3, features=5

output, (h_n, c_n) = lstm(x)

print("Output:", output)
print("Hidden state:", h_n)
print("Cell state:", c_n)

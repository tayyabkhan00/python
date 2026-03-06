import torch
import torch.nn as nn

rnn = nn.RNN(input_size=5, hidden_size=10, num_layers=1, batch_first=True)

# sample input: batch=1, seq_length=3, features=5
x = torch.randn(1, 3, 5)

output, hidden = rnn(x)

print("Output:", output)
print("Hidden:", hidden)

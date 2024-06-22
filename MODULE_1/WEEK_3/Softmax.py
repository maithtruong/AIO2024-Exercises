"""
    Define a Softmax class which is derived from the Module class.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        return F.softmax(x, dim=-1)
    
class SoftmaxStable:

    def __call__(self, x):
        max_val, _ = torch.max(x, dim=-1, keepdim=True)
        exps = torch.exp(x - max_val)
        softmax_probs = exps / torch.sum(exps, dim=-1, keepdim=True)
        return softmax_probs

def main():
    data = torch.Tensor([1, 2, 3])
    
    softmax = Softmax()
    output = softmax(data)
    print("Standard softmax:", output)
    
    softmax_stable = SoftmaxStable()
    output_stable = softmax_stable(data)
    print("Stable softmax:", output_stable)

if __name__ == "__main__":
    main()

import torch;
import torch.nn as nn
import torch.optim as optim
import csv
import random
import numpy as np
class Adder(nn.Module):
 def __init__(self):
  super().__init__()
  self.hidden1=nn.Linear(2,5)
  self.act1=nn.ReLU()
  self.hidden2=nn.Linear(5,2)
  self.act2=nn.ReLU()
  self.output=nn.Linear(2,1)
 def forward(self,x):
  x = self.act1(self.hidden1(x))
  x = self.act2(self.hidden2(x))
  return x

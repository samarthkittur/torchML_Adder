import torch;
import torch.nn as nn
import torch.optim as optim
import csv
import random
import numpy as np
model=Adder()
test=torch.tensor([3456,9278],dtype=torch.float32);
def testAdder(x,y):
  input=torch.tensor([x,y],dtype=torch.float32);
  return model(input)
##x and y are numbers  

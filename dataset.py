import torch;
import torch.nn as nn
import torch.optim as optim
import csv
import random
import numpy as np
addend1=[];
addend2=[];
for x in range(100000):
 addend1.append(random.randint(0,100));
for y in range(100000):
 addend2.append(random.randint(0,100));
sumslst=[];
for z in range(100000):
 sumslst.append(addend1[z]+addend2[z]);
'''
#with open('additiondataset1.csv','w',newline='') as file:
  writer=csv.writer(file);
  for x in range(100000):
#  writer.writerow([addend1[x],addend2[x],sumslst[x]])
'''
device=("mps" if torch.backends.mps.is_available() else "cpu");
dataset=np.loadtxt('additiondataset1.csv',delimiter=',');
X=dataset[:,0:2];
y=dataset[:,2];
X=torch.tensor(X,dtype=torch.float32);
y=torch.tensor(y,dtype=torch.float32).reshape(-1,1);

import torch;
import torch.nn as nn
import torch.optim as optim
import csv
import random
import numpy as np  
model=Adder()
loss_fn=nn.MSELoss()
optimizer=optim.Adam(model.parameters(),lr=0.001)
n_epochs=10
batch_size=100

for epoch in range(n_epochs):
    for i in range(0, len(X), batch_size):
        Xbatch = X[i:i+batch_size]
        y_pred = model(Xbatch)
        ybatch = y[i:i+batch_size]
        loss = loss_fn(y_pred, ybatch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f'Finished epoch {epoch}, latest loss {loss}')
  
with torch.no_grad():
    y_pred = model(X)
accuracy = (y_pred.round() == y).float().mean()
print(f"Accuracy {accuracy}")

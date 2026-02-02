import torch
from torch import nn
import torch.nn.functional as F
import numpy as np

device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"

class CNN(nn.Module):
    def __init__(self,input_shape,num_actions):
        super(CNN, self).__init__()
        self.convolutional_blocks = nn.Sequential(
            nn.Conv2d(input_shape[0], 64, kernel_size=(3,4), stride=(3,4), padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=(1,2), stride=(1,2), padding=1),
            nn.ReLU()
            )
        self.fcl_blocks = nn.Sequential(
            nn.Linear(self.convolutional_output_units(input_shape), 128),
            nn.ReLU(),
            nn.Linear(128, num_actions)
            )         
    def convolutional_output_units(self, shape):
        dummy_input = torch.zeros(1, *shape)
        dummy_output = self.convolutional_blocks(dummy_input)
        size = int(np.prod(dummy_output.size()))
        return size

    def forward(self, x):         
        convolutional_output = self.convolutional_blocks(x).view(x.size()[0], -1)
        fcl_output = self.fcl_blocks(convolutional_output)        
        return fcl_output
    
class ANN(nn.Module):
    def __init__(self,input_shape,num_actions):
        super(ANN,self).__init__()
        
        self.fcl_blocks = nn.Sequential(
            nn.Flatten(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, num_actions),
            )
    def forward(self, x):
        fcl_output = self.fcl_blocks(x)        
        return fcl_output
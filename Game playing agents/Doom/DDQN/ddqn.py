#imports
import numpy as np
import torch 
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torchvision.models
from torchvision.models import MobileNet_V2_Weights
import time
import torch.utils.data as data_utils
from collections import deque
import random 


class Net_A(nn.Module):
    def __init__(self,input_shape,num_actions):

        super(Net_A, self).__init__()
        
        self.conv_blocks = nn.Sequential(
            nn.Conv2d(input_shape[0], 64, kernel_size=(3,4), stride=(3,4), padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=(1,2), stride=(1,2), padding=1),
            nn.ReLU()
            )
        self.fcl_blocks = nn.Sequential(
            nn.Linear(self.conv_output_units(input_shape), 128),
            nn.ReLU(),
            nn.Linear(128, num_actions)
            )
              
    def conv_output_units(self, shape):
        dummy_input = torch.zeros(1, *shape)
        dummy_output = self.conv_blocks(dummy_input)
        size = int(np.prod(dummy_output.size()))
        return size

    def forward(self, x):
        conv_out = self.conv_blocks(x).view(x.size()[0], -1)
        fcl_out = self.fcl_blocks(conv_out)
        return fcl_out

class Net_B(nn.Module):
    def __init__(self,input_shape,num_actions):

        super(Net_B, self).__init__()
        
        self.mobile_net = torchvision.models.mobilenet_v2(weights=MobileNet_V2_Weights.DEFAULT)
        
        for param in self.mobile_net.parameters():
            param.requires_grad = False
        self.model = []
        
        block_num = 6
        
        for block in range(block_num):
            self.model.append(self.mobile_net.features[block])
        
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(self.conv_output_units(input_shape), 256),
            nn.ReLU(),
            nn.Linear(256, num_actions)
            )
                    
    def conv_output_units(self, shape):
        x = torch.zeros(1, *shape)
        for idx in range(len(self.model)):
            x = self.model[idx](x)
        size = int(np.prod(x.size()))
        return size
        
    def forward(self, x):
        for idx in range(len(self.model)):
            x = self.model[idx](x)
        x = self.classifier(x)
        x = x.view(x.size()[0], -1)
        return x

class Net_C(nn.Module):

    def __init__(self, input_shape, num_actions):
        super(Net_C, self).__init__()
        
        self.flat = nn.Flatten()
        self.layer1 = nn.Linear(np.prod(input_shape), 128)
        self.layer2 = nn.Linear(128, 128)
        self.layer3 = nn.Linear(128, num_actions)

    def forward(self, x):
        x = self.flat(x)
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        return self.layer3(x)

#DDQN agent
class DDQN:
    def __init__(self, 
                 state_size, 
                 action_size, 
                 gamma, 
                 epsilon_decay,
                 replay_memory, 
                 target_update, 
                 batch_size=32,
                 network='A'):
        
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=replay_memory)
        self.gamma = gamma  
        self.epsilon = 1  
        self.epsilon_min = 0.01
        self.epsilon_decay = epsilon_decay
        self.target_update = target_update
        self.target_counter = 0
        self.batch_size = batch_size
        self.network = network
        self.device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
        self.main_model = self._build_model()
        self.target_model = self._build_model()
        self.target_model.load_state_dict(self.main_model.state_dict())
        self.main_criterion = criterion = nn.MSELoss()
        self.main_optim = optim.Adam(filter(lambda p: p.requires_grad, self.main_model.parameters()),
                                     lr=0.001,
                                     eps=1e-7)
        
    def _build_model(self):
        
        if self.network=='A':
            net = Net_A(self.state_size,self.action_size).to(self.device)
        elif self.network=='B':
            net = Net_B(self.state_size,self.action_size).to(self.device)
        else:
            net = Net_C(self.state_size,self.action_size).to(self.device)
            
        return net

    def remember(self, state, action, reward, next_state, done):        
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):       
        if np.random.rand() <= self.epsilon: 
            return np.random.randint(self.action_size)
        
        net_input = torch.tensor(state).to(self.device)
        net_input = torch.unsqueeze(net_input, 0)
        with torch.no_grad():
            q_value_esimates = self.main_model(net_input)
        action = torch.argmax(q_value_esimates).item()
        return action
    
    #train DDQN
    def train(self):
        
        minibatch = random.sample(self.memory, self.batch_size)
        
        states = torch.tensor(np.array([memory[0] for memory in minibatch])).to(self.device)
        next_states = torch.tensor(np.array([memory[3] for memory in minibatch])).to(self.device)
        
        with torch.no_grad():
            Q = self.target_model(next_states)
        predictions = self.main_model(states)
        prediction_targets = predictions.detach().clone()
        
        for index in range(self.batch_size):               
            target = torch.tensor(minibatch[index][2])+torch.tensor((1-minibatch[index][4]))*self.gamma*torch.max(Q[index])
            prediction_targets[index][minibatch[index][1]]=target
         
        self.main_optim.zero_grad()
        loss = self.main_criterion(predictions,prediction_targets)
        loss.backward()
        self.main_optim.step()
        
        #update target model
        self.target_counter+=1
        if self.target_counter==self.target_update-1:
            self.target_counter=0
            self.target_model.load_state_dict(self.main_model.state_dict())
        #apply epsilon decay
        if self.epsilon > self.epsilon_min:
            self.epsilon -= self.epsilon_decay
        else:
            self.epsilon = self.epsilon_min

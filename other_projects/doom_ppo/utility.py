import torch
from PIL import Image
from torchvision.transforms import functional as F, ToPILImage
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

def constants(num_actions,null_state_shape):
    actions = [[i==j for i in range(num_actions)] for j in range(num_actions)]
    null_state = null_state_shape[1:]
    null_state = np.zeros(null_state)
    return actions,null_state

def resize(raw_pixels,resolution,scale): 
    if scale: raw_pixels=raw_pixels/255.0  
    img = Image.fromarray(raw_pixels)
    img = img.resize(resolution[::-1])   
    return F.to_tensor(img) 

def plot(rewards,kills):
    plt.plot(rewards)
    plt.plot(savgol_filter(rewards, min(51,len(rewards)), 3))
    plt.title("Reward per episode")
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.show()
    plt.clf()

    plt.plot(kills)
    plt.plot(savgol_filter(kills, min(51,len(kills)), 3))
    plt.title("Kills per episode")
    plt.xlabel('Episode')
    plt.ylabel('Kills')
    plt.show()
    plt.clf()
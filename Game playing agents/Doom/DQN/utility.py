import torch
from PIL import Image
from torchvision.transforms import functional as F, ToPILImage
import matplotlib.pyplot as plt
import numpy as np

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

def plot(rewards):
    plt.plot(rewards)
    plt.title("Reward per episode")
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.show()

def view_frame(img):
    to_pil = ToPILImage()
    image = to_pil(img)
    image.show()
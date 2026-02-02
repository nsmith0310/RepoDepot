from vizdoom import *
import random, time
import ddqn, utility
from collections import deque
import numpy as np
import torch
from flask import Flask, Response
from PIL import Image
import io

app = Flask(__name__)

device_name = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
device = torch.device(device_name)

numpy_seed = 0
np.random.seed(numpy_seed)
random.seed(0) 
torch_seed = 0
torch.manual_seed(torch_seed); None

if device_name != "cpu":
    torch.cuda.manual_seed(torch_seed); None
    torch.cuda.manual_seed_all(torch_seed); None
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    
#network selection
network = 'mobilenet'

#scenario selection 
scenario, num_actions, reward_shaping = ["deadly_corridor.cfg",7,200]

#vizdoom frame parameters
resize_resolution = (60,80) 
scale_pixels = False

#frame stacking and skipping
frames = 4 if network=='scratchnet' else 3
skip = 4 if network=='scratchnet' else 3

state_size = (frames,resize_resolution[0],resize_resolution[1])

actions, null_state = utility.constants(num_actions,state_size)

num_actions = len(actions)

#DDQN hyperparameters
batch_size = 32
gamma = .95
epsilon_decay = 0.0001
target_update = 1024
replay_memory = 16384

agent = ddqn.DDQN(state_size, num_actions, gamma, epsilon_decay,replay_memory,
                target_update,batch_size=batch_size,network=network)

agent.load_trained_model()


game = DoomGame()
game.load_config(scenario)
game.set_screen_resolution(vizdoom.ScreenResolution.RES_640X480)
game.set_screen_format(vizdoom.ScreenFormat.GRAY8)
game.set_window_visible(False)
game.set_seed(10)
game.init()  
    
def run_demo():
        
    while True:      
        #start new episode
        game.new_episode()
        
        #short-term memory
        stm = deque(maxlen=frames)
        for i in range(frames-1):
            null_memory = utility.resize(null_state,resize_resolution,scale_pixels)   
            stm.append(null_memory.squeeze(0))
             
        #get starting state and scale down 
        state = game.get_state().screen_buffer
        
        color_frame = np.stack([state]*3, axis=-1)
        
        state = utility.resize(state,resize_resolution,scale_pixels).squeeze(0) 
             
        stm.append(state)
        state = np.asarray(stm)
        
        while not game.is_episode_finished():
            # Choose an action
            action = agent.act(state)
        
            for k in range(frames):       
                #game.make_action(actions[action],skip)
                game.make_action(actions[action],skip)
                #check if game is finished
                done = game.is_episode_finished()
            
                if done:                    
                    break
                
                next_state = game.get_state().screen_buffer
                
                color_frame = color_frame = np.stack([next_state]*3, axis=-1)
                img = Image.fromarray(color_frame, 'RGB')               
                buffer = io.BytesIO()
                img.save(buffer, format="JPEG")
                jpg_bytes = buffer.getvalue()
                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + jpg_bytes + b"\r\n"
                )
                
                next_state = utility.resize(next_state,resize_resolution,scale_pixels).squeeze(0)
                                
                stm.append(next_state)
                next_state = np.asarray(stm)
                time.sleep(0.1)
                
            # Update the state
            state = np.copy(next_state)
            
            if done:                
                break
                
            

@app.route("/video")
def video():
    return Response(
        run_demo(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )

@app.route("/")
def index():
    return """
        <!DOCTYPE html>
        <html>
        <head>
          <title>VizDoom Demo</title>
          <style>
            body {
              display: flex;
              flex-direction: column; 
              justify-content: center; 
              align-items: center;     
              height: 100vh;
              margin: 0;
              background-color: #000;  
              color: white;
              font-family: 'Impact', sans-serif; 
            }
        
            h1 {
              color: red;
              font-size: 5em;          
              margin: 0.2em 0 0.5em 0; 
              text-shadow: 2px 2px 4px #000; 
            }
            h2 {
              color: red;
              font-size: 2em;          
              margin: 0.1em 0 0.2em 0; 
              text-shadow: 2px 2px 4px #000; 
            }
        
            img {
              max-width: 90%;
              max-height: 80%;
              border: 4px solid red;   
            }
          </style>
        </head>
        <body>
          <h1>DOOM</h1>
          <h2>VizDoom Corridor Demo<h2>
          <img src="/video" alt="VizDoom Demo">
        </body>
        </html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

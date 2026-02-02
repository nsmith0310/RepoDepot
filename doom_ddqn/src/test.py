from vizdoom import *
import random, time
import ddqn, utility
from collections import deque
import numpy as np
import torch

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

scenario, num_actions, reward_shaping = ["deadly_corridor.cfg",7,200]

#vizdoom frame parameters
visible = False
resize_resolution = (60,80) 
scale_pixels = False

#frame stacking and skipping
frames = 4 if network=='scratchnet' else 3
skip = 4 if network=='scratchnet' else 3

state_size = (frames,resize_resolution[0],resize_resolution[1])

actions, null_state = utility.constants(num_actions,state_size)

num_actions = len(actions)

#initialize vizdoom
game = DoomGame()
game.load_config(scenario)
game.set_window_visible(visible)
game.set_screen_resolution(vizdoom.ScreenResolution.RES_640X480)
game.set_screen_format(vizdoom.ScreenFormat.GRAY8)
game.set_seed(3)
game.init()


#DDQN hyperparameters
batch_size = 32
gamma = .95
epsilon_decay = 0.0001
target_update = 1024
replay_memory = 16384

agent = ddqn.DDQN(state_size, num_actions, gamma, epsilon_decay,replay_memory,
                target_update,batch_size=batch_size,network=network)

agent.load_trained_model()

num_tests = 500
wins = 0
total_kills = 0
total_time = 0

print("Testing trained model.")
print()

for test in range(num_tests):
    
    start_time = time.time()
    episode_durations = 10000
    
    #short-term memory
    stm = deque(maxlen=frames)
    for i in range(frames-1):
        null_memory = utility.resize(null_state,resize_resolution,scale_pixels)   
        stm.append(null_memory.squeeze(0))
        
    #start new episode
    game.new_episode()

    #get starting state and scale down 
    state = game.get_state().screen_buffer      
    state = utility.resize(state,resize_resolution,scale_pixels).squeeze(0) 
    stm.append(state)
    state = np.asarray(stm)
    
    for t in range(episode_durations):
        # Choose an action
        action = agent.act(state)
    
        for k in range(frames):       
            game.make_action(actions[action],skip)
            #check if game is finished
            done = game.is_episode_finished()
        
            #set next state based on done and scale down
            if done:
                next_state = null_state
            else:
                next_state = game.get_state().screen_buffer
            
            next_state = utility.resize(next_state,resize_resolution,scale_pixels).squeeze(0)
                       
            stm.append(next_state)
            next_state = np.asarray(stm)
        
        # Update the state
        state = np.copy(next_state)
        
        if done or t==episode_durations-1:
            won = game.get_total_reward() > 0
            if won:
                message = "Victory"
            else:
                message = "Defeat"
            duration = round(time.time() - start_time,3)
            num_kills = int(game.get_game_variable(KILLCOUNT))
            print("Test "+str(test+1)+"/"+str(num_tests)+": "+message+"; number of kills: "+ \
                  str(num_kills)+"; duration: "+str(duration))
            total_kills += num_kills 
            wins += won
            total_time += duration
            break
print()
print("Testing finished.")
print("Total wins: "+str(wins)+"/"+str(num_tests))
print("Total kills: "+str(total_kills))
print("Total testing time (s): "+ str(round(total_time,3)))
print("Average number of kills per trial: "+str(round(total_kills/num_tests,3)))
print("Average time per trial: "+str(round(total_time/num_tests,3)))
         

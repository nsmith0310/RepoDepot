from vizdoom import *
import random, time
import dqn, utility
from collections import deque
import numpy as np

#scenario loader
scenarios = \
    [["basic.cfg",3,0], #0
     ["my_way_home.cfg",3,0], #1
     ["defend_the_center.cfg",3,200], #2
     ["deadly_corridor.cfg",7,200], #3
     ["health_gathering_supreme.cfg",3,0], #4
     ["deathmatch.cfg",20,0]] #5

#network selection
network = 'B'

#scenario selection
scenario_idx = 3   
scenario, num_actions, reward_shaping = scenarios[scenario_idx]

#vizdoom frame parameters
visible = False
resize_resolution = (60,80) 
scale_pixels = False

#frame stacking and skipping
frames = 4 if network=='A' else 3
skip = 4 if network=='A' else 3

state_size = (frames,resize_resolution[0],resize_resolution[1])

actions, null_state = utility.constants(num_actions,state_size)

num_actions = len(actions)

#rewards and kills
reward_scaling = 1
reward_kills = True
kill_count = 0

#initialize vizdoom
game = DoomGame()
game.load_config(scenario)
game.set_window_visible(visible)
game.set_screen_resolution(vizdoom.ScreenResolution.RES_640X480)
game.set_screen_format(vizdoom.ScreenFormat.GRAY8)
game.init()

print("scenario="+scenario[:-4])

#DQN hyperparameters
batch_size = 32
gamma = .95
epsilon_decay = 0.0001
target_update = 1024
replay_memory = 16384

agent = dqn.DQN(state_size, num_actions, gamma, epsilon_decay,replay_memory,
                target_update,batch_size=batch_size,network=network)
          
#training
training_episodes = 8000 
episode_durations = 1000
rewards = []

for episode in range(training_episodes):
    
    #short-term memory
    stm = deque(maxlen=frames)
    for i in range(frames-1):
        null_memory = utility.resize(null_state,resize_resolution,scale_pixels)   
        stm.append(null_memory.squeeze(0))
    
    print("Episode "+str(episode+1)+":")
    
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
        reward = 0
        for k in range(frames):       
            # Perform the action and scale down
            reward += game.make_action(actions[action],skip)/reward_scaling
        
            #get number of kills and reward if increased based on agent constant
            kills = int(game.get_game_variable(KILLCOUNT))
            if kills!=kill_count and reward_kills:
                reward+=(reward_shaping)/reward_scaling
                kill_count=kills
            
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
            
        # Remember the experience
        
        agent.remember(state, action, reward, next_state, done)
        
        # Update the state
        state = np.copy(next_state)

        # Check if episode is finished and if so, display metrics
        if done or t==episode_durations-1:
            print("Episode "+str(episode+1)+" over. Total reward: "+str(game.get_total_reward()))
            print("Died="+str(game.is_player_dead())+"; timesteps="+str(t)+"; kills="+str(kills))
            print("Epsilon="+str(agent.epsilon))                      
            print()
            rewards.append(game.get_total_reward())
            break
            
        # Train the agent       
        if len(agent.memory)>batch_size:
            agent.train()

            
utility.plot(rewards)        
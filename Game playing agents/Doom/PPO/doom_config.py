from vizdoom import *
import utility
from collections import deque
import numpy as np
import torch

class DOOM_GAME:
    def __init__(self,scenario,reward_shaping,resolution,scale_pixels,skip_mode):
        
        scenarios = \
            [["basic.cfg",3], #0
             ["my_way_home.cfg",3], #1
             ["defend_the_center.cfg",3], #2
             ["deadly_corridor.cfg",7], #3
             ["health_gathering_supreme.cfg",3], #4
             ["deathmatch.cfg",20]] #5
            
        self.scenario = scenarios[scenario][0]
        
        self.num_actions = scenarios[scenario][1]
        
        self.reward_shaping = reward_shaping
        
        self.resolution = resolution
        
        self.scale_pixels = scale_pixels
                
        self.frames = 4 
        
        self.skip = 4 
        
        self.skip_mode = skip_mode
        
        self.input_shape = (self.frames,self.resolution[0],self.resolution[1])

        self.actions_ohe, self.null_state = utility.constants(self.num_actions,self.input_shape)

        self.num_actions = len(self.actions_ohe)

        self.kill_count = 0

        self.game = DoomGame()
        
        self.game.load_config(self.scenario)
        
        self.game.set_window_visible(False)
        
        self.game.set_screen_resolution(vizdoom.ScreenResolution.RES_640X480)
        
        self.game.set_screen_format(vizdoom.ScreenFormat.GRAY8)
        
        self.game.init()
        
        self.stm = deque(maxlen=self.frames)
        
        for i in range(self.frames-1):
            null_memory = utility.resize(self.null_state,self.resolution,self.scale_pixels)   
            self.stm.append(null_memory.squeeze(0))
            
        self.episode_counter = 1
        self.rewards = []
        self.kill_list = []
    
    def reset(self):
        self.kill_count = 0
        self.stm = deque(maxlen=self.frames)        
        for i in range(self.frames-1):
            null_memory = utility.resize(self.null_state,self.resolution,self.scale_pixels)   
            self.stm.append(null_memory.squeeze(0))         
        self.game.new_episode()
        state = self.game.get_state().screen_buffer      
        state = utility.resize(state,self.resolution,self.scale_pixels).squeeze(0) 
        self.stm.append(state)
        state = np.asarray(self.stm)
        return state
    
    def step(self,action):
        reward = 0
        
        for k in range(self.frames):   
            
            reward += self.game.make_action(self.actions_ohe[action],self.skip)
            
            kills = int(self.game.get_game_variable(KILLCOUNT))
            if kills!=self.kill_count:
                reward+=self.reward_shaping
                self.kill_count=kills
            
            done = self.game.is_episode_finished()
        
            if done:
                next_state = self.null_state
            else:
                next_state = self.game.get_state().screen_buffer
            
            next_state = utility.resize(next_state,self.resolution,self.scale_pixels).squeeze(0)
            
            self.stm.append(next_state)
            next_state = np.asarray(self.stm)
            if self.skip_mode==1:
                return next_state,reward,done
            
        return next_state,reward,done
        
    def end(self):
        final_reward = self.game.get_total_reward()
        final_kills = self.kill_count
        self.rewards.append(final_reward)
        self.kill_list.append(final_kills)
        print("Episode "+str(self.episode_counter)+": reward: "+str(final_reward)+"; kills: "+str(final_kills))
        self.episode_counter+=1
        
    def plot(self):
        utility.plot(self.rewards,self.kill_list)
        
        
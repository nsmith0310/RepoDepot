from network import CNN,ANN
import torch
import numpy as np
from torch.distributions import MultivariateNormal, Categorical
from torch.optim import Adam

class PPO:
    def __init__(self,env):
        self._hyperparameters()
        self.environment = env
        self.observation_dims = env.input_shape
        self.action_dims = env.num_actions
        self.device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
        
        self.actor = CNN(self.observation_dims,self.action_dims).to(self.device)
        self.critic = CNN(self.observation_dims,1).to(self.device)
        
        
        self.actor_optimizer = Adam(self.actor.parameters(), lr=self.lr, eps=self.eps)
        self.critic_optimizer = Adam(self.critic.parameters(), lr=self.lr, eps=self.eps)

    def _hyperparameters(self):
        self.timesteps_per_batch = 1600
        self.max_timesteps_per_episode = 1600
        self.gamma = .99
        self.n_updates_per_iteration = 10
        self.clip = .1
        self.lr = 0.003
        self.eps = 1e-7
        self.use_annealing = True
        self.use_entropy = True
        self.entropy_coefficient = .02
        self.use_clipping = True
        self.lbda = .95
        self.max_grad_norm = 1
        
    def rollout(self):
        batch_observations = []
        batch_actions = []
        batch_log_probabilities = []
        batch_rewards = []
        batch_lengths = []
        batch_values = []
        batch_dones = []
        
        episode_rewards = []
        episode_values = []
        episode_dones = []
        
        timer = 0
        while timer < self.timesteps_per_batch:
            episode_rewards = []
            episode_values = []
            episode_dones = []
            
            observation = self.environment.reset()
            done = False
            
            for episode_timer in range(self.max_timesteps_per_episode):
                episode_dones.append(done)
                timer+=1
                batch_observations.append(observation)
                action,log_probability = self.get_action(observation)
                observation_input = torch.tensor(observation, dtype=torch.float, device=self.device).unsqueeze(0)
                value = self.critic(observation_input)
                observation,reward,done = self.environment.step(action)
                episode_rewards.append(reward)
                batch_actions.append(action)
                batch_log_probabilities.append(log_probability)
                episode_values.append(value.flatten())
                if done:
                    self.environment.end()
                    break
            batch_lengths.append(episode_timer+1)
            batch_rewards.append(episode_rewards)
            batch_values.append(episode_values)
            batch_dones.append(episode_dones)
            
        batch_observations = torch.tensor(batch_observations,dtype=torch.float,device=self.device)
        batch_actions = torch.tensor(batch_actions,dtype=torch.float,device=self.device)
        batch_log_probabilities = torch.tensor(batch_log_probabilities,dtype=torch.float,device=self.device)
        return batch_observations, batch_actions, batch_log_probabilities, batch_rewards, batch_lengths, batch_values,batch_dones
    
    def get_action(self,observation):
        observation = torch.tensor(observation, dtype=torch.float, device=self.device).unsqueeze(0)
        
        action_logits = self.actor(observation)
        distribution = torch.nn.functional.softmax(action_logits, dim=-1)
        distribution = Categorical(distribution)
        action = distribution.sample()
        log_probability = distribution.log_prob(action)
        return action.detach(),log_probability.detach()
    
    def evaluate(self,batch_observations,batch_actions):
        V = self.critic(batch_observations).squeeze()
        action_logits = self.actor(batch_observations)
        distribution = torch.nn.functional.softmax(action_logits, dim=-1)
        distribution = Categorical(distribution)
        
        log_probabilities = distribution.log_prob(batch_actions)
        return V, log_probabilities, distribution.entropy()
    
    def calculate_gae(self, rewards, values, dones):
        batch_advantages = []
        for episode_rewards, episode_values, episode_dones in zip(rewards, values, dones):
            advantages = []
            last_advantage = 0
    
            for t in reversed(range(len(episode_rewards))):
                if t + 1 < len(episode_rewards):
                    delta = episode_rewards[t] + self.gamma * episode_values[t+1] * (1 - episode_dones[t+1]) - episode_values[t]
                else:
                    delta = episode_rewards[t] - episode_values[t]
    
                advantage = delta + self.gamma * self.lbda * (1 - episode_dones[t]) * last_advantage
                last_advantage = advantage
                advantages.insert(0, advantage)
    
            batch_advantages.extend(advantages)
    
        return torch.tensor(batch_advantages, dtype=torch.float, device=self.device)   
    
    def learn(self,step_limit):
        timesteps = 1
        while timesteps < step_limit+1:
            batch_observations, \
            batch_actions, \
            batch_log_probabilities, \
            batch_rewards, \
            batch_lengths, \
            batch_values,\
            batch_dones = self.rollout()
            timesteps+=np.sum(batch_lengths)
            advantage_k = self.calculate_gae(batch_rewards, batch_values, batch_dones)
            V = self.critic(batch_observations).squeeze()
            batch_rewards_to_go = advantage_k + V.detach()
            for epoch in range(self.n_updates_per_iteration):
                if self.use_annealing:
                    fraction = (timesteps - 1.0) / step_limit
                    new_lr = max(0.0,self.lr * (1.0 - fraction))
                    self.actor_optimizer.param_groups[0]["lr"] = new_lr
                    self.critic_optimizer.param_groups[0]["lr"] = new_lr

                V, current_log_probabilities,entropy = self.evaluate(batch_observations, batch_actions)
                ratios = torch.exp(current_log_probabilities - batch_log_probabilities)
                surrogate_loss_1 = ratios*advantage_k
                surrogate_loss_2 = torch.clamp(ratios,1-self.clip,1+self.clip)*advantage_k
                
                actor_loss = (-torch.min(surrogate_loss_1,surrogate_loss_2)).mean()
                entropy_loss = entropy.mean()*self.use_entropy
                actor_loss = actor_loss - entropy_loss*self.entropy_coefficient
                critic_loss = torch.nn.MSELoss()(V, batch_rewards_to_go) 
                
                self.actor_optimizer.zero_grad()
                actor_loss.backward()
                if self.use_clipping:
                    torch.nn.utils.clip_grad_norm_(self.actor.parameters(), self.max_grad_norm)
                self.actor_optimizer.step()
                        
                self.critic_optimizer.zero_grad()
                critic_loss.backward()
                if self.use_clipping:
                    torch.nn.utils.clip_grad_norm_(self.critic.parameters(), self.max_grad_norm)
                self.critic_optimizer.step()


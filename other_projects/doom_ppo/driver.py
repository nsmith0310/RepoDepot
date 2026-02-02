import ppo
import doom_config

scenario = 3
reward_shaping = 500
resolution = (60,80)
scale_pixels = True
skip_mode = 1

environment = doom_config.DOOM_GAME(scenario, reward_shaping, resolution, scale_pixels, skip_mode)

timesteps = 200000
doom_agent = ppo.PPO(environment)
doom_agent.learn(timesteps)
environment.plot()
Note: The relevant datasets have not been uploaded due to file size. If you would like the datasets, please reach out to me at
nicholas.m.smith.ai@gmail.com

Doom (NO EXTERNAL DATASETS REQUIRED)
Agents seek to win scenarios in the video game Doom (using the vizdoom library)
-aid in understanding frame skipping:
 https://danieltakeshi.github.io/2016/11/25/frame-skipping-and-preprocessing-for-deep-q-networks-on-atari-2600-games/

DDQN (Doom)
-core DDQN code adapted from and developed based on code from: 
 https://medium.com/@hkabhi916/mastering-convolutional-deep-q-learning-with-pytorch-a-comprehensive-guide-0114742a0a62
-uses a DDQN either trained from scratch or using MobileNetV2 base
-both variants are capable of winning scenarios including the corridor scenario 

PPO (Doom)
-core PPO code adapted from and developed based on code from: 
 https://medium.com/analytics-vidhya/coding-ppo-from-scratch-with-pytorch-part-1-4-613dfc1b14c8
-uses PPO
-capable of winning scenarios including the corridor scenario
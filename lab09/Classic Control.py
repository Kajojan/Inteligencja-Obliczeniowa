import gym
import numpy as np 
    
env=gym.make("MountainCarContinuous-v0", render_mode="human")


observation, info = env.reset(seed=42)
action_set=[-1,1,1]
for i in range(500):
   action = env.action_space.sample()
   action =action_set[i%3]  
   print(action)
   observation, reward, terminated, truncated, info = env.step([action])

   if terminated or truncated:
      observation, info = env.reset()
env.close()

#cigły zmiennoprzecinkowy

import gym
import numpy as np 
    
env = gym.make('FrozenLake8x8-v1',map_name="8x8" ,render_mode="human")

observation, info = env.reset(seed=42)

for _ in range(2000):
   action = env.action_space.sample()
   print(action)
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()
env.close()



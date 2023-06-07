import  gym
import numpy as np 


env=gym.make('Taxi-v3',render_mode="human" )
# env = gym.make('HalfCheetah-v2', render_mode="human")

observation, info = env.reset(seed=42)
action_set = [1,1,1,4,3,3,3,0,0,3,3,3,0,5]  # Akcje: 0 (w dół), 1 (w górę), 2 (w lewo), 3 (w prawo), 4 (pickup), 5 (drop off)

for i in range(19):
   action = action_set[i]
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()
env.close()
#zestaw akcji skońcozny  dyskretne 


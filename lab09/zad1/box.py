import gym

env = gym.make("CarRacing-v2", render_mode="human")
observation = env.reset()
total_reward = 0

# Główna pętla
while True:
    env.render()

    action = env.action_space.sample()  


    observation, reward, done, truncated, info = env.step(action)

    total_reward += reward

    if done:
        break

print("Total Reward:", total_reward)

env.close()

#przestrzeń akcji ciagła "box"

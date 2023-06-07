import gym

# Tworzenie środowiska Mountain Car
env = gym.make("CarRacing-v2", render_mode="human")
# Inicjalizacja obserwacji i nagród
observation = env.reset()
total_reward = 0

# Główna pętla
while True:
    # Rysowanie środowiska
    env.render()

    # Wybór akcji
    action = env.action_space.sample()  # Przykład losowej akcji

    # Wykonanie akcji

    observation, reward, done, truncated, info = env.step(action)

    total_reward += reward

    # Sprawdzenie warunku zakończenia
    if done:
        break

# Wypisanie wyniku
print("Total Reward:", total_reward)

# Zamknięcie środowiska
env.close()

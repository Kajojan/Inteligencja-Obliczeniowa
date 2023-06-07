import gym
import pygad
import numpy 

gene_space = [0, 1,2,3]

map = [
    "SFFFFFFF",
    "FFFFFFFF",
    "FFFHFFFF",
    "FFFFFHFF",
    "FFFHFFFF",
    "FHHFFFHF",
    "FHFFHFHF",
    "FFFHFFFG",
]


def fitness_func(solution, solution_idx):
    fit = 0
    x = 0
    y = 0
    for i in solution:
        match i:
            case 0:
                if y - 1 == 8 or y - 1 == -1:
                    fit -= 10
                    continue
                elif map[x][y - 1] == "F":
                    y -= 1
                elif map[x][y - 1] == "H":
                    fit -= 2000
                    x = 0
                    y = 0
                    break
                    

                elif map[x][y - 1] == "G":
                    fit += 10000
                    y -= 1
                    break
            case 3:
                if x - 1 == 8 or x - 1 == -1:
                    fit -= 10
                    continue
                elif map[x - 1][y] == "F":
                    x -= 1
                elif map[x - 1][y] == "H":
                    fit -= 2000
                    x = 0
                    y = 0
                    break

                elif map[x - 1][y] == "G":
                    fit += 10000
                    x -= 1
                    break

            case 2:
                if y + 1 == 8 or y + 1 == -1:
                    fit -= 10
                    continue
                elif map[x][y + 1] == "F":
                    y += 1
                elif map[x][y + 1] == "H":
                    fit -= 2000
                    x = 0
                    y = 0
                    break

                elif map[x][y + 1] == "G":
                    fit += 10000
                    y += 1
                    break
            case 1:
                if x + 1 == 8 or x + 1 == -1:
                    fit -= 10
                    continue
                elif map[x + 1][y] == "F":
                    x += 1
                elif map[x + 1][y] == "H":
                    fit -= 2000
                    x = 0
                    y = 0
                    break
                elif map[x + 1][y] == "G":
                    fit += 10000
                    x += 1
                    break

    fit += (numpy.abs(x - 7) + numpy.abs(y - 7))*-1
    # print(fit)
    return fit
# # Definicja funkcji fitness
# def fitness_function(solution, sol_idx):
#     # Stworzenie środowiska gry FrozenLake8x8
#     env = gym.make("FrozenLake8x8-v1", is_slippery=False)
#     action = solution[0]
#     # Resetowanie środowiska
#     observation = env.reset()
    
#     # Wykonanie ruchów na podstawie chromosomu
#     for action in solution:
#         # Wykonanie akcji w środowisku
#         observation = env.step(action)[0]
#         reward = env.step(action)[1]
#         print(env.step(action))
#         done = env.step(action)[2]
#         # Jeśli osiągnięto cel lub upłynęło zbyt wiele kroków, zakończ grę
#         if done:
#             break
    
#     # Obliczenie wartości fitness
#     fitness = reward
#     print(fitness)
#     return fitness*-1

# Stworzenie instancji algorytmu genetycznego
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=500, 
                       sol_per_pop=200, 
                       num_genes=16, 
                       num_parents_mating=10, 
                       fitness_func=fitness_func)

# Uruchomienie algorytmu genetycznego
ga_instance.run()

# Wyświetlenie najlepszego rozwiązania znalezionego przez algorytm genetyczny dla FrozenLake8x8
best_solution = ga_instance.best_solution()
print("Najlepsze rozwiązanie dla FrozenLake8x8:", best_solution)

env = gym.make('FrozenLake8x8-v1', map_name="8x8", render_mode="human",is_slippery=False)

# Resetowanie środowiska
observation, info = env.reset(seed=42)
# Wykonanie ruchów na podstawie najlepszego rozwiązania
for action in best_solution[0]:
    action = int(action)
    # action=1
    observation, reward, terminated, truncated, info = env.step(action)
    env.render()
   
    if terminated:
        break

# Zamknięcie środowiska
env.close()

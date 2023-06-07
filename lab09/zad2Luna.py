import gym
import pygad
import numpy

# Funkcja fitness ocenia jakość rozwiązania
gene_space = [0, 1,2,3]
def fitness_function(solution, sol_idx):
    # Tworzenie środowiska gry LunarLander
    env = gym.make("LunarLander-v2")

    observation = env.reset()
    x=0
    y=0
    for action in solution:
        # print(env.step(action))
        observation, reward, done,info,_ = env.step(action)

        if done:
            x = observation[0]
            y = observation[1]
            break
    
    fitness = reward - (numpy.abs(x ) + numpy.abs(y ))

    if(reward==-100):
        fitness+=1000

    return fitness*-1


num_generations = 2000
population_size = 600

# Tworzenie instancji algorytmu genetycznego
ga_instance = pygad.GA(gene_space=gene_space,
                        num_generations=num_generations, 
                       sol_per_pop=population_size, 
                       mutation_type=None,
                       num_genes=300, 
                       gene_type=int, 
                       num_parents_mating=50, 
                       fitness_func=fitness_function)

# Uruchomienie algorytmu genetycznego
ga_instance.run()

# Wyświetlenie najlepszego rozwiązania
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Najlepsze rozwiązanie: {solution}".format(solution=solution))
print("Wartość fitness najlepszego rozwiązania: {fitness}".format(fitness=solution_fitness))


env = gym.make("LunarLander-v2", render_mode="human")

# Resetowanie środowiska
observation, info = env.reset(seed=42)
# Wykonanie ruchów na podstawie najlepszego rozwiązania
for action in solution:
    action = int(action)
    # action=1
    observation, reward, terminated, truncated, info = env.step(action)
    # print(reward)

    env.render()
   
    if terminated:
        break

# Zamknięcie środowiska
env.close()

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
        observation, reward, done,info,_ = env.step(action)

        if done:
            x = observation[0]
            y = observation[1]
            break
    
    fitness = reward - (numpy.abs(x ) + numpy.abs(y ))

    if(reward==-100):
        fitness+=100000

    return fitness*-1


num_generations = 500
population_size = 200

ga_instance = pygad.GA(gene_space=gene_space,
                        num_generations=num_generations, 
                       sol_per_pop=population_size, 
                       mutation_type=None,
                       num_genes=300, 
                       gene_type=int, 
                       num_parents_mating=50, 
                       fitness_func=fitness_function)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Najlepsze rozwiązanie: {solution}".format(solution=solution))
print("Wartość fitness najlepszego rozwiązania: {fitness}".format(fitness=solution_fitness))


env = gym.make("LunarLander-v2", render_mode="human")

observation, info = env.reset(seed=42)
for action in solution:
    action = int(action)
    observation, reward, terminated, truncated, info = env.step(action)
    env.render()
   
    if terminated:
        break

env.close()

import pygad
import numpy
import time


gene_space = [0, 1]

items = [{'item': 'zegar', 'value': 100, 'weight': 7},
         {'item': 'obraz-pejzaż', 'value': 300, 'weight': 7},
         {'item': 'obraz-portret', 'value': 200, 'weight': 6},
         {'item': 'radio', 'value': 40, 'weight': 2},
         {'item': 'laptop', 'value': 500, 'weight': 5},
         {'item': 'lampka nocna', 'value': 70, 'weight': 6},
         {'item': 'srebrne sztućce', 'value': 100, 'weight': 1},
         {'item': 'porcelana', 'value': 250, 'weight': 3},
         {'item': 'figura z brązu', 'value': 300, 'weight': 10},
         {'item': 'skórzana torebka', 'value': 280, 'weight': 3},
         {'item': 'odkurzacz', 'value': 300, 'weight': 15}]

def fitness_func(solution, solution_idx):
    weight =0
    value = 0
    for i in range(0,len(solution)):
        if(solution[i]==1):
            weight += items[i]["weight"]
            value += items[i]["value"]
    if(weight<=25):
        fitness=value
    else:
        fitness=0
    return fitness

fitness_function = fitness_func
sol_per_pop = 11
num_genes = len(items)


num_parents_mating = 5
num_generations = 30
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 8

srednia=[]
for i in range(0,10):
    start=time.time()
    ga_instance = pygad.GA(gene_space=gene_space,
                        num_generations=num_generations,
                        num_parents_mating=num_parents_mating,
                        fitness_func=fitness_function,
                        sol_per_pop=sol_per_pop,
                        num_genes=num_genes,
                        parent_selection_type=parent_selection_type,
                        keep_parents=keep_parents,
                        crossover_type=crossover_type,
                        mutation_type=mutation_type,
                        mutation_percent_genes=mutation_percent_genes,
                        stop_criteria=["reach_1600"])
    ga_instance.run()
    end=time.time()
    srednia.append(end-start)
solution, solution_fitness, solution_idx = ga_instance.best_solution()


solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

for i in range(0,len(solution)):
        if(solution[i]==1):
           print(items[i]["item"])

print("srednia czas", sum(srednia)/len(srednia))

print("Number of generations passed is {generations_completed}".format(generations_completed=ga_instance.generations_completed))
ga_instance.plot_fitness()


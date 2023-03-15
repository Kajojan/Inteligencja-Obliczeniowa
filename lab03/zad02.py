import numpy
import pygad

lab = [      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
             [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
             [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1 ,1],
             [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ]

gene_space =[0,1,2,3] #0-dół 1-góra 2-prawo 3-lewo 



def fitness_func(solution, solution_idx):
    x=1
    y=1
    for i in solution:
        match i:
            case 0:
                if(lab[x+1][y] == 0):
                    x+=1
                elif(lab[x-1][y] == 3):
                    x+=1
                    break
            case 1:
                if(lab[x-1][y] == 0):
                    x-=1
                elif(lab[x-1][y] == 3):
                    x-=1
                    break
            case 2:
                if(lab[x][y+1] == 0):
                    y+=1
                elif(lab[x][y+1] == 3):
                    y+=1
                    break
            case 3:
                if(lab[x][y-1] == 0):
                    y-=1
                elif(lab[x][y-1] == 3 ):
                    y-=1
                    break
    fitness=-(numpy.abs(x-10) + numpy.abs(y-10))
    # print(fitness)
    return fitness

fitness_function = fitness_func


sol_per_pop = 300
num_genes = 30

num_parents_mating = 150
num_generations = 50
keep_parents = 2
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 4

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
                        mutation_percent_genes=mutation_percent_genes)
ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()



solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))


ga_instance.plot_fitness()
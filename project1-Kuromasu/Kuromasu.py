import numpy as np
import pygad
import random
plansza = [  [0, 1, 0, 0,0],
             [0, 0, 0, 0,0],
             [0, 0, 2, 0,0],
             [0, 1, 0, 0,0] ]



def fitness_func(solution, solution_idx):
    helper = plansza
    print("sol", solution)
    for coord in solution:
        x, y = coord
        if helper[x][y] == 0:
            helper[x][y]=-1
    print(*helper, sep="\n")

    
    # for x in range(len(plansza)):
    #     for y in range(len(plansza)):

    score = 0 #ile liczb sie zgadza 
    liczb = 0 #ile pól z liczbami 
    black = [] #czarne potrzebne 
    kara = 0
    for row in range(len(helper)):
        for col in range(len(helper[row])):
            # print(helper[row][col] )
            if helper[row][col] == 0:  # puste pole
                continue
            elif helper[row][col] > 0:  # pole z liczbą
                count = 0
                liczb += 1
                # licz białe pola poziomo w prawo od pola z liczbą
                for i in range(col+1, len(helper[row])):
                    if helper[row][i] == -1:  # czarne pole
                        if [row,i] not in black:
                            black.append([row,i])
                        break
                    else:  # białe pole z liczbą
                        count += 1
                # licz białe pola poziomo w lewo od pola z liczbą
                for i in range(col-1, -1, -1):
                    if helper[row][i] == -1:  # czarne pole
                        if [row,i] not in black:
                            black.append([row,i])
                        break
                    else : # puste pole
                        count += 1
                # licz białe pola pionowo w dół od pola z liczbą
                for i in range(row+1, len(helper)):
                    if helper[i][col] == -1:  # czarne pole
                        if [row,i] not in black:
                            black.append([row,i])
                        break
                    else:  # białe pole z liczbą
                        count += 1
                        
                # licz białe pola pionowo w górę od pola z liczbą
                for i in range(row-1, -1, -1):
                    if helper[i][col] == -1:  # czarne pole
                        if [row,i] not in black:
                            black.append([row,i])
                        break
                    else:  # białe pole z liczbą
                        count += 1
                if count == helper[row][col]:
                    score += 1
            else:
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    x = row + dx
                    y = col + dy
                    if x >=0 and y >= 0 and x<len(helper) and y<len(helper) :
                        if helper[x][y] == -1:
                            kara=100
                            break

    fitness=( (score/liczb * 100)  ) - (len(solution)-len(black)) - kara
    if fitness < 0 :
        fitness=0
    return fitness



fitness_function = fitness_func

sol_per_pop = 300
num_genes = random.randint(1, (len(plansza)*len(plansza))/2)
# gene_space = range(4),range(4)
gene_space = [np.array([i, j]) for i in range(4) for j in range(4)]
# gene_type = np.array([np.array([0, 0])] * num_genes, dtype=object)
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
                        mutation_percent_genes=mutation_percent_genes,
                        )
ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()



solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))


ga_instance.plot_fitness()
# print(fitness_func([[1,1],[0,2],[2,3],[3,2],[2,0]]))
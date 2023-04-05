import numpy as np
import pygad
import copy
from plansze import liczba, gene_space

def fitness(plansza):
    def fitness_func(solution, solution_idx):
        helper = copy.deepcopy(plansza)

        kara = 0
        kara2 = 0
        for coord in range(0,len(solution),2) :
            # print(solution[coord],solution[coord+1])
            if helper[solution[coord]][solution[coord+1]] == 0:
                helper[solution[coord]][solution[coord+1]] = -1
            elif helper[solution[coord]][solution[coord+1]] == -1:
                kara=100
            else:
                kara2+=100
        score = 0 #ile liczb sie zgadza 
        liczb = 0 #ile pól z liczbami 
        black = [] #czarne potrzebne 
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

        fitness=(score/liczb * 100) - kara 
        # print(helper)

        return fitness
    

    sol_per_pop = 1000  #100 # #350 300
    num_genes = liczba*2
    num_parents_mating = 100
    num_generations =300  #300  #20
    keep_parents = 2
    parent_selection_type = "sss"
    crossover_type = "single_point"
    mutation_type = "random"
    mutation_percent_genes = 4
    fitness_function=fitness_func
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
                                gene_type=int
                                )
    ga_instance.run()

    return ga_instance.best_solution()



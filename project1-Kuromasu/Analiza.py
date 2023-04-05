from Kuromasu import *
from plansze import liczba, plansze, gene_space
import random
import pandas as pd
import time
import matplotlib.pyplot as plt
from pso import *



setki={}
for i in range(0,2):
    plansza=plansze[random.randint(0,2)]
    start=time.time()
    # solution, solution_fitness, solution_idx = fitness(plansza)
    best_score = pso_solve(plansza,100,10000)
    end=time.time()    
    print(setki.keys())
    if  best_score[1]*-1 in setki.keys():
                setki[best_score[1]*-1].append([best_score[0],end-start])
    else:
                setki[best_score[1]*-1]=[[best_score[0], end-start]]

    # if  "{solution_fitness}".format(solution_fitness=solution_fitness) in setki.keys() :
    #             setki["{solution_fitness}".format(solution_fitness=solution_fitness)].append(["{solution}".format(solution=solution),end-start])
    # else:
    #         setki["{solution_fitness}".format(solution_fitness=solution_fitness)]=[[("{solution}".format(solution=solution)),end-start ]]


print(setki)
print("wyniki 100% to", len(setki[100.0]) ,"% całości ")
s=0
for i in setki[100.0]:
    s+=i[1]
    print(i[0],"\n")
print("sredni czas dla setek ", s/len(setki[100.0]))

import csv


# zapis do pliku

with open('./dane3.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    for key in setki:
        for i in setki[key]:
            print()
            writer.writerow(['5x5', key, i[1]])




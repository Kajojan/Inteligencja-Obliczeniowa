from Kuromasu import *
from plansze import liczba, plansze, gene_space
import random
import pandas as pd
import time
import matplotlib.pyplot as plt



setki={}
for i in range(0,100):
    plansza=plansze[random.randint(0,2)]
    start=time.time()
    solution, solution_fitness, solution_idx = fitness(plansza)
    end=time.time()    

    if  "{solution_fitness}".format(solution_fitness=solution_fitness) in setki.keys() :
                setki["{solution_fitness}".format(solution_fitness=solution_fitness)].append(["{solution}".format(solution=solution),end-start])
    else:
            setki["{solution_fitness}".format(solution_fitness=solution_fitness)]=[[("{solution}".format(solution=solution)),end-start ]]

print(setki)
print("wyniki 100% to", len(setki["100.0"]) ,"% całości ")
s=0
for i in setki["100.0"]:
    s+=i[1]
    print(i[0],"\n")
print("sredni czas dla setek ", s/len(setki["100.0"]))

import csv

# przykładowe dane

# zapis do pliku
with open('./dane.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    # writer.writerow(['Kategoria', 'Wartość'])
    for key in setki:
        for i in setki[key]:
            print()
            writer.writerow(['5x5', key, i[1]])




import numpy as np
import pyswarms as ps
import copy

def optimize_func(solution,board):
            helper = copy.deepcopy(board)
            kara = 0
            kara2 = 0
            solution2 = solution.reshape((len(helper),len(helper)))
            for i in range(0,len(solution)):
                if solution[i]==1:
                    if helper[i//len(solution2)][i % len(solution2)] == 0:
                        helper[i//len(solution2)][i % len(solution2)] = -1
                    elif helper[i//len(solution2)][i % len(solution2)] == -1:
                        kara=100
                    else:
                        kara2+=10

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

            fitness=(score/liczb * 100) - kara -kara2

            return fitness*-1


def fitness_function(positions, board):

    positions = np.array(positions)

    fitness = np.zeros(len(positions))

    for i, solution in enumerate(positions):

        fitness[i]=optimize_func(solution,board)

    return fitness
    


def pso_solve(kuromasu_board, num_particles, max_iter):

    # Inicjalizacja rozmiarów planszy i obliczenie liczby komórek planszy
    num_cells = len(kuromasu_board)*len(kuromasu_board)
    # Inicjalizacja położeń cząstek oraz ich prędkości
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9, "k":2, "p":2}
    optimizer = ps.discrete.binary.BinaryPSO(n_particles=num_particles, dimensions=num_cells, options=options)
    best_pos, best_cost = optimizer.optimize(fitness_function, iters=max_iter, board=kuromasu_board)

    return best_cost, best_pos


# plansze =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 4, 8, 0],
#              [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 6, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 9, 0, 0, 0, 0],
#              [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
#              [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# print(pso_solve(plansze, 15, 100000))
import numpy as np
import copy

def fitness_function(board, solution):
    # Ensure black cells are not adjacent
    for i, cell in enumerate(solution):
        if cell == 1:
            x, y = np.unravel_index(i, board.shape)
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for neighbor in neighbors:
                if (0 <= neighbor[0] < board.shape[0] and 
                    0 <= neighbor[1] < board.shape[1] and 
                    board[neighbor] == 1):
                    return -1  # Invalid solution

    # Ensure all white cells have the correct number of adjacent black cells
    total_score = 0
    for i, cell in enumerate(solution):
        if cell == 0:
            x, y = np.unravel_index(i, board.shape)
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            adjacent_blacks = 0
            for neighbor in neighbors:
                if (0 <= neighbor[0] < board.shape[0] and 
                    0 <= neighbor[1] < board.shape[1] and 
                    solution[np.ravel_multi_index(neighbor, board.shape)] == 1):
                    adjacent_blacks += 1
            if adjacent_blacks == board[x][y]:
                total_score += 1
    print(total_score)
    return total_score




def pso_solve(kuromasu_board, num_particles, max_iter):
    # kuromasu_board = np.array(plansza)
    # Inicjalizacja rozmiarów planszy i obliczenie liczby komórek planszy
    # board_shape = kuromasu_len(board)
    num_cells = len(kuromasu_board)*len(kuromasu_board)

    # Inicjalizacja położeń cząstek oraz ich prędkości
    particles_pos = np.random.randint(0, 2, size=(num_particles, num_cells))
    particles_vel = np.zeros((num_particles, num_cells))

    # Inicjalizacja najlepszego położenia globalnego i jego wartości funkcji fitness
    global_best_pos = np.zeros(num_cells, dtype=np.int8)
    global_best_fitness = np.inf

    # Obliczenie wartości funkcji fitness dla każdej cząstki i aktualizacja najlepszego położenia lokalnego
    particles_fitness = np.zeros(num_particles)
    for i in range(num_particles):
        particles_fitness[i] = fitness_function(kuromasu_board, particles_pos[i])
        print(particles_fitness[i])
        # print(global_best_fitness)
        if particles_fitness[i] > global_best_fitness:
            global_best_fitness = particles_fitness[i]
            global_best_pos = particles_pos[i].copy()

    # Pętla główna algorytmu PSO
    for iter in range(max_iter):
        # Obliczenie nowych prędkości dla każdej cząstki
        particles_vel = 0.5 * particles_vel + 2 * np.random.rand(num_particles, num_cells) * (particles_pos - particles_pos.mean(axis=0))
        particles_vel = np.clip(particles_vel, -1, 1)

        # Aktualizacja położeń cząstek na podstawie ich prędkości
        particles_pos = np.clip(particles_pos + particles_vel, 0, 1)
        # print(particles_pos)

        # Obliczenie wartości funkcji fitness dla każdej cząstki i aktualizacja najlepszego położenia lokalnego
        for i in range(num_particles):
            particles_fitness[i] = fitness_function(kuromasu_board, particles_pos[i])
            if particles_fitness[i] < fitness_function(kuromasu_board, global_best_pos):
                global_best_fitness = particles_fitness[i]
                global_best_pos = particles_pos[i].copy()
    print(global_best_fitness)
    # Zwrócenie najlepszego znalezionego rozwiązania
    return global_best_pos



# board = np.array([[2, 0, 0, 0, 0],
#                   [0, 4, 0, 0, 0],
#                   [0, 0, 0, 0, 0],
#                   [0, 0, 0, 6, 0],
#                   [0, 0, 0, 0, 1]])

# num_particles = 15
# max_iter = 150
# result = pso_solve(board, num_particles, max_iter)
# solution, score = result[0], result[1]
# print(result)


# import matplotlib.pyplot as plt


# data = {'100.0': [['[2 4 0 4 0 1 4 4 3 0 4 3 1 2 1 1]', 0.6419591903686523], 
#                   ['[3 1 3 3 4 4 1 0 4 4 4 2 0 1 1 3]', 0.6447005271911621], 
#                   ['[0 3 1 0 4 4 1 2 2 4 3 3 4 3 4 4]', 0.6351587772369385], 
#                   ['[2 3 1 1 1 1 0 3 3 0 2 1 4 2 1 2]', 0.6118736267089844], 
#                   ['[3 3 2 1 4 2 3 3 1 2 2 3 3 0 0 3]', 0.6080048084259033], 
#                   ['[0 0 0 0 2 0 0 1 4 0 4 0 4 1 4 3]', 0.6238901615142822], 
#                   ['[1 2 2 4 0 0 0 1 3 0 0 4 4 3 4 4]', 0.6272687911987305], 
#                   ['[2 1 0 1 4 4 4 3 0 4 0 0 3 0 2 4]', 0.6300694942474365], 
#                   ['[4 4 0 1 1 2 4 2 3 0 3 3 3 4 0 0]', 0.4986138343811035]], 
#         '66.66666666666666': [['[1 1 4 0 1 1 1 2 2 1 4 4 4 2 1 1]', 0.5953068733215332]]}

# # Sumowanie wartości dla każdej etykiety
# label_sums = {}
# for key, value in data.items():
#     for item in value:
#         label = key
#         score = item[1]
#         if label not in label_sums:
#             label_sums[key] = score
#         else:
#             label_sums[key] += score
# # Wykres kołowy dla wynikowych wartości
# plt.pie(list(label_sums.values()), labels=list(label_sums.keys()))
# plt.show()



import matplotlib.pyplot as plt

times = []
scores = []
for k, v in my_dict.items():
    for item in v:
        times.append(item[1])
        scores.append(float(k))

# utwórz wykres
plt.scatter(times, scores)
plt.xlabel('Czas wykonania')
plt.ylabel('Procentowa poprawność')
plt.title('Wykres')
plt.show()

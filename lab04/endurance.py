import pyswarms as ps
import math 
import numpy as np
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
def endurance(array):
    return -(math.exp(-2*(array[1]-math.sin(array[0]))**2)+math.sin(array[2]*array[3])+math.cos(array[4]*array[5]))

x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)


def f(x):
    n_particles = x.shape[0]
    j = [endurance(x[i]) for i in range(n_particles)]
    return np.array(j)


optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6,
options=options, bounds=my_bounds)
optimizer.optimize(f, iters=1000)
cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()

#from _future_ import division
import tsplib95
import acopy
from satsp import solver

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

problem = tsplib95.load('machine-learning/Instances/berlin52.tsp')

print(problem.is_depictable())
print(problem.display_data_type)

cities = []
if(problem.display_data_type == "TWOD_DISPLAY"):
    data = problem.display_data
else:
    data = problem.node_coords

print(len(data))
for i in range(0, len(data)):
    print(i+1, data[i+1][0], data[i+1][1])
    other_list = [i+1, data[i+1][0], data[i+1][1]]
    cities.append(other_list)


#solver.Solve(cities,epochs=10000)
solver.Solve(cities, stopping_count=300)
solver.PrintSolution()
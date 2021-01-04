#from _future_ import division
import tsplib95
import acopy
from satsp import solver

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

problem = tsplib95.load('machine-learning/Instances/bays29.tsp')

G = problem.get_graph()
n = list(G.edges)

cities = []
i = 1
for x in n:
    y = list(x)
    y.insert(0, i)
    cities.append(y)
    i += 1

solver.Solve(cities)
solver.PrintSolution()
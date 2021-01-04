import tsplib95
import acopy
import networkx as nx

solver = acopy.Solver(rho=.03, q=1)
colony = acopy.Colony(alpha=1, beta=3)

problem = tsplib95.load('machine-learning/Instances/burma14.tsp')
G = problem.get_graph()

tour = solver.solve(G, colony, limit=100)
print(tour.cost)
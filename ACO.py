#importing needed libraries
import tsplib95
import acopy
import networkx as nx
import matplotlib.pyplot as plt
import time

#set timer start time
start_time = time.time()

#setting setup variables
solver = acopy.Solver(rho=.03, q=1)
colony = acopy.Colony(alpha=1, beta=3)

#load problem from file
problem = tsplib95.load('machine-learning/Instances/ch150.tsp')
G = problem.get_graph()

#calling function from library to solve TSP
tour = solver.solve(G, colony, limit=100)

#Printing result information
print("Best TSP tour length: %d" %tour.cost)
print("Best TSP tour: %s" %tour.path)
print("Time taken: %s seconds" %(time.time() - start_time))

#sketching the graph for the resulting TSP
_, ax = plt.subplots()
pos = problem.display_data or problem.node_coords
nx.draw_networkx_nodes(G, pos=pos, ax=ax, node_color="brown")
nx.draw_networkx_labels(G, pos=pos, labels={i: str(i) for i in range(1, len(G.nodes) + 1)}, font_size=8, font_color='white')

solution = tour.path
path = solution

nx.draw_networkx_edges(G, pos=pos, edgelist=path, edge_color="black")
# If this doesn't exsit, x_axis and y_axis's numbers are not there.
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.show()
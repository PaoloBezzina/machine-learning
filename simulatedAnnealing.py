import tsplib95
import acopy

solver = acopy.Solver(rho=.03, q=1)
colony = acopy.Colony(alpha=1, beta=3)

problem = tsplib95.load_problem('bays29.tsp')
G = problem.get_graph()
tour = solver.solve(G, colony, limit=100)
#importing necessary libraries
import tsplib95
import time
from satsp import solver

#load problem from file
problem = tsplib95.load('machine-learning/Instances/pr76.tsp')

#set timer start time
start_time = time.time()

#reading nodes/coords accordingly depending on the type defined in the file
cities = []
if(problem.display_data_type == "TWOD_DISPLAY"):
    data = problem.display_data
else:
    data = problem.node_coords

#adding all nodes to a list of cities to be travalled to
for i in range(0, len(data)):
    print(i+1, data[i+1][0], data[i+1][1])
    other_list = [i+1, data[i+1][0], data[i+1][1]]
    cities.append(other_list)

#calling the function to solve the tsp from the library SAtsp
solver.Solve(cities, stopping_count=300)    #solver.Solve(cities,epochs=1000)
print("Time taken: %s seconds" %(time.time() - start_time))
solver.PrintSolution()
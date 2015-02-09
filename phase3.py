# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 20:53:34 2015

This is the optimization phase. The edge matrix generated in phase 2 will be
optimized for differential probablity using Ant Colony Optimization.
"""

class Ant:
    tour_length = 0      # Ant's tour length
    tour = [0] * 257     # Ant's memory storing tours
    visited = [0] * 256  # Visited cities

def construct_ant_solution():
    """
        ConstructAntsSolutions manages a colony of ants that concurrently and 
        asynchronously visit adjacent states of the considered problem by moving 
        through neighbor nodes of the problem’s construction graph GC. They move 
        by applying a stochastic local decision policy that makes use of pheromone 
        trails and heuristic information. In this way, ants incrementally build 
        solutions to the optimization problem. Once an ant has built a solution, 
        or while the solution is being built, the ant evaluates the (partial) 
        solution that will be used by the UpdatePheromones procedure to decide how
        much pheromone to deposit.
    """
    pass


def update_pheromone():
    """
        UpdatePheromones is the process by which the pheromone trails are modified. The
        trails value can either increase, as ants deposit pheromone on the components or
        connections they use, or decrease, due to pheromone evaporation From a practical 
        point of view, the deposit of new pheromone increases the probability that 
        those components/connections that were either used by many ants or that were 
        used by at least one ant and which produced a very good solution will be used 
        again by future ants. Di¤erently, pheromone evaporation implements a useful 
        form of forgetting: it avoids a too rapid convergence of the algorithm
        toward a suboptimal region, therefore favoring the exploration of new areas of the
        search space.
    """
    pass

def daemon_actions():
    """
        DaemonActions procedure is used to implement centralized actions
        which cannot be performed by single ants. Examples of daemon actions are the 
        activation of a local optimization procedure, or the collection of global 
        information that can be used to decide whether it is useful or not to deposit 
        additional pheromone to bias the search process from a nonlocal perspective. 
        As a practical example, the daemon can observe the path found by each ant in 
        the colony and select one or a few ants (e.g., those that built the best 
        solutions in the algorithm iteration) which are then allowed to deposit 
        additional pheromone on the components/connections they used.
    """
    pass

def run_aco(dist):
    """
        Run ACO using ACS on the adjacency matrix
    """
    nlist = [[] for i in range(256)]       # Nearest neighbour matrix
    pheromone = [[5 for j in range(256)] for i in range(256)]   # Initial Pheromone Setup
    choice_info = [[0 for j in range(256)] for i in range(256)] # Combined pheromone and heuristic value
    a = [Ant() for i in range(5)]
    alpha = 1    
    beta = 2
    # Data Initialization
    # nlist contains indices in ascending order of the nodes in terms of DP
    for i in range(256):
        b = {}
        for m,n in enumerate(dist[i]):
            b[n] = []
        for m,n in enumerate(dist[i]):
            b[n].append(m)
        for m in b:
            for n in b[m]:
                nlist[i].append(n)
    
    for i in range(256):
        for j in range(256):
            if dist[i][j] == 0:
                eta = 1/0.00001
            else:
                eta = 1/dist[i][j]
            choice_info[i][j] = (pheromone[i][j]**alpha)*(eta**beta)
    return choice_info
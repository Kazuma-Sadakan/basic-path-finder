from queue import PriorityQueue 

# class Graph:
#     def __init__(self, num_of_vertices):
#         self.v = num_of_vertices 
#         self.edges = [[-1 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
#         self.visited = []

#     def add_edge(self, u, v, weight):
#         self.edges[u][v] = weight 
#         self.edges[v][u] = weight 

#     def dijkstra(self, start_vertex):
#         D = {v: float('inf') for v in range(self.v)}
#         D[start_vertex] = 0

#         pq = PriorityQueue()
#         pq.put((0, start_vertex))
#         while not pq.empty:
#             (dist, current_vertex) = pq.get()
#             self.visited.append(current_vertex)

#             for neighbor in range(self.v):
#                 if self.edges[current_vertex][neighbor] != -1:
#                     distance = self.edges[current_vertex][neighbor]
#                     if neighbor not in self.visited:
#                         old_cost = D[neighbor]
#                         new_cost = D[current_vertex] + distance
#                         if new_cost < old_cost:
#                             pq.put((new_cost, neighbor))
#                             D[neighbor] = new_cost 


#         return D 

from queue import PriorityQueue
from graph import WeightedGraph

def dijkstras_search(graph, start, goal):
    frontier = PriorityQueue()
    came_from = {}
    cost_so_far = {node: float("inf") for node in graph.edges.keys()}
    came_from[start] = None 
    cost_so_far[start] = 0 
    frontier.put((start,cost_so_far[start]))

    while not frontier.empty(): 
        current_node, cost = frontier.get() 
        

        if current_node == goal:
            break

        for next in graph.get_neighbers(current_node):
            new_cost = cost_so_far[current_node] + graph.get_cost(current_node, next)
            if new_cost < cost_so_far[next]:
                print(next, "|", new_cost)
                cost_so_far[next] = new_cost
                frontier.put((next, new_cost))
                came_from[next] = current_node
            print("-", came_from)
    return came_from, cost_so_far

# def dijkstras_search(blocks, start, goal):
#     frontier = PriorityQueue()
#     came_from = {}
#     cost_so_far = {block: float("inf") for row in blocks for block in row}
#     came_from[start] = None 
#     cost_so_far[start] = 0 
#     frontier.put((start,cost_so_far[start]))

#     while not frontier.empty(): 
#         current_block, cost = frontier.get() 

#         if current_block == goal:
#             break

#         for next in current_block.get_neighbers():
#             next.set_role(SERCHED)
#             next.draw()
#             new_cost = cost_so_far[current_block] + 1
#             if new_cost < cost_so_far[next]:
#                 cost_so_far[next] = new_cost
#                 frontier.put((next, new_cost))
#                 came_from[next] = current_block

    # return came_from, cost_so_far

weighted_graph = WeightedGraph()
weighted_graph.edges = {
    "A": [("B", 1)],
    "B": [("C", 2)],
    "C": [("B", 4), ("D", 2), ("F", 2)],
    "D": [("C",1), ("E", 1)],
    "E": [("F", 1)],
    "F": []
}

print(dijkstras_search(weighted_graph, "A", "E"))







                    

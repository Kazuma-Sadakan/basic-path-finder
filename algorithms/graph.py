class Graph:
    def ___init__(self):
        # {"A": ["S", "B", "D"],
        # "B": ["S", "A", "D", "H"],
        # "C": ["S", "L"],
        # "D": ["A", "B", "F"],
        # "E": ["K", "G"],
        # "F": ["D", "H"],
        # "G": ["H", "E"],
        # "H"}
        self.edges = {} 
    def get_neighbors(self, current_node):
        return self.edges[current_node]

class Node:
    def __init__(self, node, weight):
        self.loc = node
        self.weight = weight 

class WeightedGraph:
    def __init__(self):
        super().__init__()
        self.edges = {} 

    def get_neighbers(self, current_node):
        return [node for node, cost in self.edges[current_node]]

    def set_cost(self, from_node, to_node): #from_node node to_node (next_node, 12)
        if from_node not in self.edges:
            self.edges[from_node] = []
            self.edges[from_node].append(to_node)
        else:
            self.edges[from_node].append(to_node)

    def get_cost(self, from_node, to_node):
        neighbers = self.edges.get(from_node, None)
        # print(neighbers)
        if neighbers is not None:
            for neighber, cost in neighbers:
                if neighber == to_node:
                    return cost
        else:
            return -1
    

# graph = Graph()
# graph.edges = {
#     "A": ["B"],
#     "B": ["C"],
#     "C": ["B", "D", "F"],
#     "D": ["C", "E"],
#     "E": ["F"],
#     "F": []
# }

# weighted_graph = WeightedGraph()
# weighted_graph.edges = {
#     "A": [("B", 1)],
#     "B": [("C", 2)],
#     "C": [("B", 2), ("D", 2), ("F", 7)],
#     "D": [("C",2), ("E", 7)],
#     "E": [("F", 3)],
#     "F": []
# }
# weighted_graph.set_cost("A", ("D", 17))
# print(weighted_graph.get_cost("A", "D"))
# print(weighted_graph.get_neighbers("C"))
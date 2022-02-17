from queue import Queue
from graph import Graph

def breadth_first_search(graph, start_node):
    frontier = Queue()
    frontier.put(start_node)
    explored = []
    explored.append(start_node)

    while not frontier.is_empty:
        current_node = frontier.get()
        print(f"visiting {current_node}")
        for next_ in graph.get_neighbors(current_node):
            if next_ not in explored:
                # print(next_)
                frontier.put(next_)
                explored.append(next_)

graph = Graph()
graph.edges = {
    "A": ["B"],
    "B": ["C"],
    "C": ["B", "D", "F"],
    "D": ["C", "E"],
    "E": ["F"],
    "F": []
}
breadth_first_search(graph, "A")
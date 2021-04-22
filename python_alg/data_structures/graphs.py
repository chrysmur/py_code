'''
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
adjacency dict
'''

# given a graph, return the edges
# edges are the connections
# vertices are the nodes

def generate_egdes(graph):
    edges = []
    for node in graph:
        for neighbor in node:
            edges.append((node, neighbor))

    return edges

def calculate_isolated(graph):
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated

class Graph:
    def __init__(self, graph_dict={}):
        # initialize an empty dict or an initial value
        self.__graph_dict = graph_dict

    def vertices(self):
        # Return the vertices of a graph
        return list(self.__graph_dict.keys())

    def edges(self):
        #Return the edges of the graph
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
            

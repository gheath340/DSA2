class Vertex:
    # Constructor for a new Vertx object. All vertex objects
    # start with a distance of positive infinity.
    def __init__(self, label, visited=False):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None
        self.Visited = visited

    def getLabel(self):
        return self.label
        
class Graph:
    def __init__(self):
        self.adjacency_list = {} # vertex dictionary {key:value}
        self.edge_weights = {} # edge dictionary {key:value}
        self.vertexList = {} # vertexID : vertex object
        
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = [] # {vertex_1: [], vertex_2: [], ...}
        self.vertexList[new_vertex.getLabel()] = new_vertex
        
    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight 
            # {(vertex_1,vertex_2): 484, (vertex_1,vertex_3): 626, (vertex_2,vertex_6): 1306, ...}
        self.adjacency_list[from_vertex].append(to_vertex) 
            # {vertex_1: [vertex_2, vertex_3], vertex_2: [vertex_6], ...}
 
    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
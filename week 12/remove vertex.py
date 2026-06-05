class graph:
    def __init__(self):
        self.graph = {
            "a": ["b", "c"],
            "b": ["a"],
            "c": ["a"],
        }
    def remove_vertex(self, vertex):
        if vertex in self.graph:
            self.graph.pop(vertex)
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)
    
    def print_graph(self):
        print(self.graph)

g = graph()
g.remove_vertex("c")
g.print_graph()
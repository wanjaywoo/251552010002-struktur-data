class graph:
    def _init_(self):
        self.graph = {
            "a": ["b", "c"],
            "b": ["a"],
            "c": ["a"]
        }
    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def print_graph(self):
        print(self.graph)

g = graph()
g.remove_edge("a", "b")
g.print_graph() 
class graph:
    def __init__(self):
        self.graph = {
            "a": ["b"],
            "b": ["a", "c"],
            "c": ["b"]
        }
    def search(self, start, target):
        visited = set ()
        def dfs(v):
            if v == target:
                return True
            visited.add(v)
            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(start)
g = graph()
print("a ke c?", g.search("a", "c"))
print("a ke d?", g.search("a", "d"))
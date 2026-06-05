class graph:
    def __init__(self):
        self.graph = {
            "a": ["b", "c"],
            "b": ["a", "d"],
            "c": ["a", "e"],
            "d": ["b"],
            "e": ["c"],
        }
    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            v = queue.pop(0)
            if v not in visited:
                visited.add(v)
                result.append(v)
                queue.extend([n for n in self.graph[v] if n not in visited])
        return result

g = graph()
print("traversal bfs dari a:", g.bfs("a"))
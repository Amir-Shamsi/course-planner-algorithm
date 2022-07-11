from collections import defaultdict

class DirectedGraph:
    def __init__(self, vertices_count):
        self._graph = defaultdict(list)
        self._vertices_count = vertices_count

    def add_edge(self, u, v):
        self._graph[u].append(v)

    def get_cyclic(self, v, visited, recursion_stack):

        visited[v] = True
        recursion_stack[v] = True
        for neighbour in self._graph[v]:
            if not visited[neighbour]:
                if self.get_cyclic(neighbour, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbour]:
                return True
        recursion_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * (self._vertices_count + 1)
        recursion_stack = [False] * (self._vertices_count + 1)
        for node in range(self._vertices_count):
            if not visited[node]:
                if self.get_cyclic(node, visited, recursion_stack):
                    return True
        return False




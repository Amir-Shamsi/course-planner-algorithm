from Data_Structures.Directed_Graph import DirectedGraph

class CourseOrdering(DirectedGraph):
    _course_graph = None
    _is_possible_to_finished = None

    def __init__(self, numCourses, prerequisites):
        super().__init__(numCourses)
        self.prerequisites = prerequisites
        self.numCourses = numCourses
        self._create_graph()

    def _create_graph(self):
        self._all_vertices = list()
        for pre_req in self.prerequisites:
            self.add_edge(pre_req[1], pre_req[0])
            self._all_vertices.append(pre_req[1])
            self._all_vertices.append(pre_req[0])

    def can_courses_be_finished(self):
        if self._is_possible_to_finished is None:
            self._is_possible_to_finished = not self.is_cyclic()
        return self._is_possible_to_finished

    def sort(self, ordered, n, visited):
        visited[n] = True
        for element in self._graph[n]:
            if not visited[element]:
                self.sort(ordered, element, visited)
        ordered.insert(0, n)

    def ordering(self):  # topological_sort
        if not self.can_courses_be_finished():
            return list()
        visited = [False] * self._vertices_count
        ordered = []
        for element in range(self._vertices_count):
            if not visited[element]:
                self.sort(ordered, element, visited)
        return ordered

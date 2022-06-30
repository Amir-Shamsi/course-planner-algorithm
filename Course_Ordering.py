from Graph.Directed_Graph import DirectedGraph

class CourseOrdering:
    _course_graph = None
    _is_possible_to_finished = None

    def __init__(self, numCourses, prerequisites):
        self.prerequisites = prerequisites
        self.numCourses = numCourses
        self._create_graph()

    def _create_graph(self):
        self._course_graph = DirectedGraph(self.numCourses)
        for pre_req in self.prerequisites:
            self._course_graph.add_edge(pre_req[0], pre_req[1])

    def can_courses_be_finished(self):
        if self._is_possible_to_finished is None:
            self._is_possible_to_finished = not self._course_graph.is_cyclic()
        return self._is_possible_to_finished


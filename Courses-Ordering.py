import numpy as np
from numpy import ndarray
from Graph.Directed_Graph import DirectedGraph

class CourseOrdering:
    _course_graph = None
    _is_possible_to_finished = None

    def __init__(self, numCourses: int, prerequisites: list[list[int]] | ndarray):
        self.prerequisites = prerequisites
        self.numCourses = numCourses

        self._create_graph()

    def _create_graph(self):
        self._course_graph = DirectedGraph(self.numCourses)
        for pre_req in self.prerequisites:
            self._course_graph.add_edge(pre_req[0], pre_req[1])


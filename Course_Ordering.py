import itertools

from data_structures.Directed_Graph import DirectedGraph


class CourseOrdering(DirectedGraph):
    _course_graph = None
    _is_possible_to_finished = None
    _courses_ordering = None
    pre_req_courses = {0: [], 1: []}

    def __init__(self, numCourses, prerequisites):
        super().__init__(numCourses)
        self.prerequisites = prerequisites
        self.numCourses = numCourses
        self._create_graph()

    def _create_graph(self):
        _remain_courses = [x for x in range(self.numCourses)]
        for pre_req in self.prerequisites:
            self.add_edge(pre_req[1], pre_req[0])

            if pre_req[0] in _remain_courses: _remain_courses.remove(pre_req[0])
            if pre_req[1] in _remain_courses: _remain_courses.remove(pre_req[1])

        for course in _remain_courses:
            self._graph[course] = []

    def can_be_taken(self):
        if self._is_possible_to_finished is None:
            self._is_possible_to_finished = not self.is_cyclic()
        return self._is_possible_to_finished

    def sort(self, ordered, n, visited):
        visited[n] = True
        for element in self._graph[n]:
            if not visited[element]:
                self.sort(ordered, element, visited)
        ordered.insert(0, n)

    def ordering(self):
        if not self.can_be_taken():
            return list()
        if self._courses_ordering is not None:
            return self._courses_ordering
        visited = [False] * self._vertices_count
        ordered = []
        for element in range(self._vertices_count):
            if not visited[element]:
                self.sort(ordered, element, visited)

        self._courses_ordering = ordered
        return ordered

    def study_plan(self, free_sems, addition_cost, max_courses):
        free_courses_flag = True
        graph = self._graph.copy()
        semesters, next_sem, visited_courses = [[]], [], []
        courses_pick_count, total_cost, semester_count = 0, 0, 0

        _s_graph_items = sorted(self.dfs_max_lens(), key=lambda course: (self.dfs_max_lens()[course][0], self.dfs_max_lens()[course][1]), reverse=True)

        while len(graph) != 0:
            for course in _s_graph_items:
                if course in next_sem or course in list(itertools.chain.from_iterable(graph.values())):
                    continue
                if courses_pick_count < max_courses:
                    semesters[semester_count].append(course)
                    next_sem.extend(graph.get(course))
                    visited_courses.append(course)
                    courses_pick_count+=1
                    if not free_courses_flag:
                        total_cost += addition_cost*(semester_count+1 - free_sems)
                else:
                    break
            semester_count+=1
            semesters.append([])
            if len(next_sem) > 0: next_sem.clear()
            courses_pick_count = 0
            free_courses_flag = (semester_count < free_sems)
            for v in visited_courses:
                graph.pop(v)
                _s_graph_items.remove(v)
            visited_courses.clear()
        semesters.pop()
        return semesters, total_cost

    def query(self, queries):
        return [(self._courses_ordering.index(query[1]) < self._courses_ordering.index(query[0])) for query in queries]

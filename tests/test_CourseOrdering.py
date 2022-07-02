from Course_Ordering import CourseOrdering

def test_CourseOrdering():  # phase 1 to 3
    numCourses = 7
    prerequisites = [[5, 4], [1, 0], [2, 1], [2, 3], [2, 0], [1, 6], [6, 0]]

    course_ordering = CourseOrdering(numCourses, prerequisites)

    print('can courses be finished?:', course_ordering.can_be_taken())

    print('ordering:', course_ordering.ordering())

    queries = [[2, 6], [2, 0], [0, 2]]
    print('for queries `{}`: {}'.format(queries, course_ordering.query(queries)))

def test_CourseOrdering_1():  # phase 4
    numCourses = 8
    # prerequisites = [[1, 0], [3, 2], [5, 2], [2, 1]]
    # prerequisites = [[1, 0], [3, 2], [5, 2], [2, 0]]
    prerequisites = [[1, 0], [3, 2], [5, 2]]
    # prerequisites = [[1, 0], [2, 0], [3, 2], [1, 3], [5, 2]]

    course_ordering = CourseOrdering(numCourses, prerequisites)

    print('can courses be finished?:', course_ordering.can_be_taken())

    print('ordering:', course_ordering.ordering())
    semesters, total_cost = course_ordering.study_plan(2, 100, 4)
    for index in range(len(semesters)):
        print('semesters #{}: {}'.format(index, semesters[index]))

    print('Cost of this plan: {}$'.format(total_cost))

    # queries = [[2, 6], [2, 0], [0, 2]]
    # print('for queries `{}`: {}'.format(queries, course_ordering.query(queries)))

if __name__ == '__main__':
    test_CourseOrdering_1()

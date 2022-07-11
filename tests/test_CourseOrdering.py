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
    numCourses = 13
    # prerequisites = [[1, 0], [3, 2], [5, 2], [2, 1]]
    # prerequisites = [[1, 0], [3, 2], [5, 2], [2, 0]]
    # prerequisites = [[1, 0], [3, 2], [5, 2]]

    # prerequisites = [[1, 0], [2, 0], [3, 2], [1, 3], [5, 2]]
    prerequisites = [[7, 11], [3, 1], [6, 2], [7, 5], [7, 10], [3, 8], [6, 8], [3, 11], [3, 10], [3, 5], [3, 0], [6, 9],
                     [3, 9], [6, 0], [7, 0], [6, 1], [3, 7], [7, 9], [6, 11], [3, 4], [3, 2], [6, 10], [3, 6], [3, 12],
                     [7, 8], [7, 12]]

    course_ordering = CourseOrdering(numCourses, prerequisites)

    print('can courses be finished?:', course_ordering.can_be_taken())

    print('ordering:', course_ordering.ordering())
    semesters, total_cost = course_ordering.study_plan(1, 100, 9)
    for index in range(len(semesters)):
        print('semesters #{}: {}'.format(index + 1, semesters[index]))

    print('Cost of this plan: {}$'.format(total_cost))

    # queries = [[2, 6], [2, 0], [0, 2]]
    # print('for queries `{}`: {}'.format(queries, course_ordering.query(queries)))

if __name__ == '__main__':
    test_CourseOrdering_1()

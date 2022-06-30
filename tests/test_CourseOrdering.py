from Course_Ordering import CourseOrdering

def test_CourseOrdering():
    numCourses = 7
    prerequisites = [[5, 4], [1, 0], [2, 1], [2, 3], [2, 0], [1, 6], [6, 0]]

    course_ordering = CourseOrdering(numCourses, prerequisites)

    print('can courses be finished?:', course_ordering.can_courses_be_finished())

    print('ordering:', course_ordering.ordering())

if __name__ == '__main__':
    test_CourseOrdering()
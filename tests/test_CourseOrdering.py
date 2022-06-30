from Course_Ordering import CourseOrdering

def test_CourseOrdering():
    numCourses = 2
    prerequisites = [[1, 0], [0, 2]]

    course_ordering = CourseOrdering(numCourses, prerequisites)

    print('can courses be finished?:', course_ordering.can_courses_be_finished())

if __name__ == '__main__':
    test_CourseOrdering()
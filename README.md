# Course Planner Algorithm
*algorithm design and analysis of the algorithm course of computer science engineering.*

There are a total of numCourses courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array prerequisites where **prerequisites[i] = [Ai, Bi]** indicates that you must take course `Bi` first if you want to take course `Ai`.
* For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

1. function `can_courses_be_finished()`:

    Return `true` if you can finish all courses. Otherwise, return `false`.
    ```
    Input: numCourses = 2, prerequisites = [[1,0]]

    Output: true

    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
    So it is possible
    ```

2. function `ordering()`:

    Return the ordering of courses student should take to finish all courses. If there are many valid answers, it returns one of them. If it is impossible to finish all courses, returns an **empty array**.
    ```
    Input: numCourses = 4, prerequisites = [[1,0], [3,1]]

    Output: [0,1,3,2]

    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
    So the correct course order is [0,1].
    ```
    
3. function `query()`:

    Prerequisites can also be indirect. If course `a` is a prerequisite of course `b` and course `b` is `a`
prerequisite of course `c`, then course `a` is `a` prerequisite of course `c`.

    You are also given an array `queries` where `queries[j] = [uj, vj]`. For the `Jth` query, you should
answer whether course `uj` is a prerequisite of course vj or not.
Return a boolean array answer, where `answer[j]` is the answer to the `Jth` query.

    <p align="center">
        <img src="doc/part3_digrapg.png" height=200/>
    </p>

    ```
    Input: numCourses = 2, prerequisites = [[1,0], [2,0], [3,2]], queries = [[0,1],[3,0]]
    
    Output: [false,true]
    
    Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
    Course 0 is not a prerequisite of course 1, and for second one prerequisites are [2,0] and [3,2] so [3,0] is true.
    ```

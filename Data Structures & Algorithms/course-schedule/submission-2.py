class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        course_map = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            course_map[crs].append(pre)

        path_set = set()

        def dfs(course):
            if course in path_set:
                return False
            if not course_map[course]:
                return True
            path_set.add(course)
            for prerequisit in course_map[course]:
                if not dfs(prerequisit):
                    return False
            path_set.remove(course)
            course_map[course] = []
            return True        
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
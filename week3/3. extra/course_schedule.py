class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict = {i :[] for i in range(numCourses)}
        visited = {i : 0 for i in range(len(dict))}
        cycle = True
        for i, j in prerequisites:
            dict[i].append(j)

        
        def dfs(point):
            nonlocal cycle
            if visited[point] == 0:
                visited[point] = 1
            elif visited[point] == 1:
                cycle = False
                return
            else:
                return
            
            for i in dict[point]:
                dfs(i)
            visited[point] = 2
        for i in range(len(dict)):
            if visited[i] != 2:
                dfs(i)
        return cycle





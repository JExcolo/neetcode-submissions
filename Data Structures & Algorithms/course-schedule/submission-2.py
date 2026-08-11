from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adjList = {}
        visited = set()
        
        for edge in prerequisites:
            if edge[0] not in adjList:
                adjList[edge[0]] = [edge[1]]
            else:
                adjList[edge[0]].append(edge[1])
            if edge[1] not in adjList:
                adjList[edge[1]] = []

        def dfs(node):
            if adjList[node] == []:
                return True
            if node in visited:
                return False
            visited.add(node)
            for edge in adjList[node]:
                if not dfs(edge):
                    return False
            adjList[node] = []
            visited.remove(node)
            return True
        for vert in adjList:
            if not dfs(vert):
                return False
        return True

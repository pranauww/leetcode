class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        preMap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        seen = set()

        def dfs(crs):
            if crs in visited:
                return False
            if crs in seen:
                return True
            
            visited.add(crs)
            for pre in preMap(crs):
                if not dfs(pre):
                    return False
            visited.remove(crs)
            seen.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return output
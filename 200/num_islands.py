class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                row, col = q.popleft()
                for dr, dc in directions:
                    tr = row + dr
                    tc = col + dc
                    if (tr in range(rows) and
                        tc in range(cols) and
                        grid[tr][tc] == "1" and
                        (tr, tc) not in visited):
                        q.append((tr, tc))
                        visited.add((tr, tc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        
        return islands
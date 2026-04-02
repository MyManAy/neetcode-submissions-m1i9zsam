class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        partOfIsland = set()
        maxSize = 0
        def numIslandsRec(i, j, visited):
            if ((i, j) in partOfIsland 
                or min(i , j) < 0 
                or i >= len(grid) 
                or j >= len(grid[0]) 
                or grid[i][j] == 0 
                or (i, j) in visited):
                return
            else:
                visited.add((i, j))
                partOfIsland.add((i, j))
                numIslandsRec(i+1, j, visited)
                numIslandsRec(i-1, j, visited)
                numIslandsRec(i, j+1, visited)
                numIslandsRec(i, j-1, visited)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                prevIslands = len(partOfIsland)
                numIslandsRec(i, j, set())
                diff = len(partOfIsland) - prevIslands
                maxSize = max(maxSize, diff)

        return maxSize
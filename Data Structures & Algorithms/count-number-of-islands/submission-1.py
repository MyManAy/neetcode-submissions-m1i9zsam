class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        partOfIsland = set()
        count = 0
        def numIslandsRec(i, j, visited):
            if ((i, j) in partOfIsland 
                or min(i , j) < 0 
                or i >= len(grid) 
                or j >= len(grid[0]) 
                or grid[i][j] == "0" 
                or (i, j) in visited):
                return
            else:
                visited.add((i, j))
                partOfIsland.add((i, j))
                numIslandsRec(i+1, j, visited)
                numIslandsRec(i-1, j, visited)
                numIslandsRec(i, j+1, visited)
                numIslandsRec(i, j-1, visited)
                visited.remove((i, j))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                prevIslands = len(partOfIsland)
                numIslandsRec(i, j, set())
                if len(partOfIsland) > prevIslands:
                    count += 1

        return count
            

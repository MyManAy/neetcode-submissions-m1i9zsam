class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in board]
        col = [set() for _ in board]
        grid = [set() for _ in board]

        for i in range(len(board)):
            for j in range(len(board[i])):
                element = board[i][j]
                gridIndex = ((i // 3) * 3) + (j // 3)

                if element == ".":
                    continue
                if element in row[i] or element in col[j] or element in grid[gridIndex]:
                    print(i, j, element)
                    if element in row[i]:
                        print(row[i])
                    if element in col[j]:
                        print(col[j])
                    if element in grid[gridIndex]:
                        print("t")
                        print("grid", gridIndex)
                        print(grid[gridIndex])
                    return False
                else:
                    row[i].add(element)
                    col[j].add(element)
                    grid[gridIndex].add(element)

        return True
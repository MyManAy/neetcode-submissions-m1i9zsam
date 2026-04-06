class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(len(board))]
        col = [set() for i in range(len(board))]
        grids = [set() for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                n = board[i][j]
                grid = j // 3 + ((i // 3) * 3)
                if n == ".":
                    continue

                if n in row[i] or n in col[j] or n in grids[grid]:
                    return False
                row[i].add(n)
                col[j].add(n)
                grids[grid].add(n)

        return True
        
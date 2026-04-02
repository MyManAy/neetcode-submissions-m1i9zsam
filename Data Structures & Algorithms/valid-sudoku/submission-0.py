class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            nums = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in nums:
                    return False
                else:
                    nums.add(board[i][j])

        for j in range(len(board)):
            nums = set()
            for i in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in nums:
                    return False
                else:
                    nums.add(board[i][j])

        for boxRow in range(0, len(board), 3):
            for boxCol in range(0, len(board), 3):
                nums = set()
                for i in range(boxRow, boxRow + 3):
                    for j in range(boxCol, boxCol + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in nums:
                            return False
                        else:
                            nums.add(board[i][j])

        return True
               
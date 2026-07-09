class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # naive approach is to traverse each row and col using hashmap for uniqueness check
        hashmap = {}

        # row-wise check
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].isnumeric():
                    if board[i][j] in hashmap:
                        return False
                    else:
                        hashmap[board[i][j]] = True
            
            hashmap.clear()
        
        hashmap.clear()

        # col-wise check
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[j][i].isnumeric():
                    if board[j][i] in hashmap:
                        return False
                    else:
                        hashmap[board[j][i]] = True
            
            hashmap.clear()
        
        hashmap.clear()

        # block-wise check (need to convert this into a generic checker for all 3x3 boxes)
        row_offset, col_offset = 0, 0
        while row_offset < 9:
            for i in range(row_offset, row_offset + 3):
                for j in range(col_offset, col_offset + 3):
                    if board[i][j].isnumeric():
                        if board[i][j] in hashmap:
                            return False
                        else:
                            hashmap[board[i][j]] = True

            hashmap.clear()

            col_offset += 3
            if col_offset >= 9:
                row_offset += 3
                col_offset = 0
            
        return True
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Pre-populate tracking sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(r, c):
            if r == 9:
                return True
            
            next_r, next_c = (r, c + 1) if c < 8 else (r + 1, 0)

            if board[r][c] != '.':
                return backtrack(next_r, next_c)

            box_idx = (r // 3) * 3 + (c // 3)
            
            for num_int in range(1, 10):
                num = str(num_int)
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    # Place number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    if backtrack(next_r, next_c):
                        return True

                    # Backtrack (remove number)
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)

            return False

        backtrack(0, 0)
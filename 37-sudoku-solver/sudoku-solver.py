class Solution(object):
    def solveSudoku(self, board):
        FULL = 511  # 0b111111111

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        # Fast population count for every possible 9-bit mask
        popcount = [0] * 512
        for i in range(1, 512):
            popcount[i] = popcount[i >> 1] + (i & 1)

        for r in range(9):
            for c in range(9):
                ch = board[r][c]

                if ch == '.':
                    empty.append((r, c, (r // 3) * 3 + c // 3))
                else:
                    bit = 1 << (ord(ch) - 49)
                    b = (r // 3) * 3 + c // 3

                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[b] |= bit

        n = len(empty)

        def solve(pos):
            if pos == n:
                return True

            best = pos
            best_count = 10

            # MRV: choose the cell with the fewest candidates
            for i in range(pos, n):
                r, c, b = empty[i]

                mask = FULL ^ (
                    (rows[r] | cols[c] | boxes[b]) & FULL
                )

                count = popcount[mask]

                if count < best_count:
                    best_count = count
                    best = i

                    if count <= 1:
                        break

            if best_count == 0:
                return False

            empty[pos], empty[best] = empty[best], empty[pos]

            r, c, b = empty[pos]
            mask = FULL ^ (
                (rows[r] | cols[c] | boxes[b]) & FULL
            )

            while mask:
                bit = mask & -mask
                mask ^= bit

                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                board[r][c] = chr(48 + bit.bit_length())

                if solve(pos + 1):
                    return True

                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit

            board[r][c] = '.'
            empty[pos], empty[best] = empty[best], empty[pos]

            return False

        solve(0)
class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = [sum(row) for row in grid]
        cols = [sum(col) for col in zip(*grid)]
        communicating = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (rows[r] > 1 or cols[c] > 1):
                    communicating += 1
        return communicating
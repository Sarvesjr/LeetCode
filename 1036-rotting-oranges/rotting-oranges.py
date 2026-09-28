class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        time,fresh = 0,0
        # find fresh and rotten oranges in grid
        ROWS,COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 :
                    fresh+=1 #count fresh
                if grid[r][c] == 2 :
                    q.append([r,c]) #add rotten to queue

        directions = [[0,1],[0,-1],[1,0],[-1,0]] #possible ways we can move in the grid

        while q and fresh > 0 :
            for i in range(len(q)): #keep spreading rotten oranges when rotten exists and fresh exists
                r,c = q.popleft() #take one rotten orange and add it to queue
                for dr, dc in directions : #check neighbours
                    row,col = dr+r, dc+c #newly rotten oranges

                    if(row<0 or row==len(grid) or col<0 or col==len(grid[0]) or grid[row][col]!=1):
                        continue #skip if outside grid or not fresh
                    grid[row][col] = 2 #make fresh orange rotten
                    q.append([row,col]) #append it to queue
                    fresh -=1 #reduce the fresh count for each orange
            time+=1 #calc time for each step
        return time if fresh == 0 else -1
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1': #if island found
                    count+=1 #store island count
                    self.traverse(grid, i, j, m, n) #visit whole island
        return count

    def traverse(self, grid, i, j, m, n):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j]=='0': #if i outside grid or in water
            return
        grid[i][j] = '0' #else mark as visited

        self.traverse(grid,i,j+1,m,n) # go right
        self.traverse(grid,i+1,j,m,n) # go down
        self.traverse(grid,i,j-1,m,n) # go left
        self.traverse(grid,i-1,j,m,n) # go up
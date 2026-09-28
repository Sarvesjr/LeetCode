class Solution {
    public int orangesRotting(int[][] grid) {

        Queue<int[]> q = new LinkedList<>();
        int fresh = 0;
        int time = 0;
        int ROWS = grid.length;
        int COLS = grid[0].length; 

        // Find all fresh and rotten oranges
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) {
                    fresh++; // Count fresh orange
                }
                if (grid[r][c] == 2) {
                    q.offer(new int[]{r, c}); // Add rotten orange to queue
                }
            }
        }
        // Right, left, down, up
        int[][] directions = {
            {0, 1},
            {0, -1},
            {1, 0},
            {-1, 0}
        };
        // Keep spreading while rotten oranges exist and fresh oranges are still left
        while (!q.isEmpty() && fresh > 0) {
            int size = q.size();
            for (int i = 0; i < size; i++) {

                int[] current = q.poll(); // Remove one rotten orange
                int r = current[0]; // Get its row
                int c = current[1]; // Get its column

                // Check all 4 directions
                for (int[] dir : directions) {
                    int row = r + dir[0]; // New row
                    int col = c + dir[1]; // New column
                    // Skip if outside grid or not fresh
                    if (row < 0 || row == ROWS ||
                        col < 0 || col == COLS ||
                        grid[row][col] != 1) {
                        continue;
                    }
                    grid[row][col] = 2; // Make fresh orange rotten
                    q.offer(new int[]{row, col}); // Add it to queue
                    fresh--; // One less fresh orange
                }
            }
            time++;
        }
        return fresh == 0 ? time : -1;
    }
}
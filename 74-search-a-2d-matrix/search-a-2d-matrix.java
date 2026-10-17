class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int r = matrix.length;
        int c = matrix[0].length;
        int total = r * c;

        int left = 0;
        int right = total - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            int rp = mid / c;
            int cp = mid % c;

            if (matrix[rp][cp] < target) {
                left = mid + 1;
            }
            else if (matrix[rp][cp] > target) {
                right = mid - 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
}
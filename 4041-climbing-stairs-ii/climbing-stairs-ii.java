class Solution {
    public int climbStairs(int n, int[] costs) {
        int v0 = 0, v1 = 0, v2 = 0;

        for (int c : costs) {
            int next = Math.min(v0 + 9, Math.min(v1 + 4, v2 + 1)) + c;
            v0 = v1;
            v1 = v2;
            v2 = next;
        }
        return v2;
    }
}
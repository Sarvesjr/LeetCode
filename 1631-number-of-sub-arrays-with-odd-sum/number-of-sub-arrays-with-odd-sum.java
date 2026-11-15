class Solution {
    public int numOfSubarrays(int[] arr) {
        long even = 1;       // Empty prefix sum is even
        long odd = 0;        // No odd prefix sum initially
        long preSum = 0;     // Running prefix sum
        long count = 0;      // Number of odd-sum subarrays

        int MOD = 1000000007;

        for (int num : arr) {
            preSum += num;

            if (preSum % 2 == 0) {
                count += odd;
                even++;
            } else {
                count += even;
                odd++;
            }

            count %= MOD;
        }

        return (int) (count % MOD);
    }
}
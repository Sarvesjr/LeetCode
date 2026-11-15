class Solution(object):
    def numOfSubarrays(self, arr):
        even = 1          # Empty prefix sum is even
        odd = 0           # No odd prefix sum initially
        preSum = 0        # Running prefix sum
        count = 0         # Number of odd-sum subarrays
        for num in arr:
            preSum += num
            if preSum % 2 == 0:
                count += odd      # Even - Odd = Odd
                even += 1
            else:
                count += even     # Odd - Even = Odd
                odd += 1
        return count % (10**9 + 7)
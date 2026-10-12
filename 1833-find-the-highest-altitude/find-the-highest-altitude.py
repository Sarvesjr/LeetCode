class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        curr, maxSum = 0, 0

        for g in gain:
            curr += g
            maxSum = max(maxSum, curr)

        return maxSum
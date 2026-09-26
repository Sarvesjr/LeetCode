class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev,curr = 1,1
        for i in range(n-1):
            curr, prev = curr+prev, curr
        return curr
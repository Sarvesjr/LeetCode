class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {0:-1}
        p = 0
        for i, num in enumerate(nums):
            p += num
            q = p%k
            if q in d:
                if i - d[q] > 1:
                    return True
            else:
                d[q] = i
        return False
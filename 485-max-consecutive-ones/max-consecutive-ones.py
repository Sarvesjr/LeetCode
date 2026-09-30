class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        l = 0

        for r in range(len(nums)):
            if nums[r]==0:
                l=r+1
            else:
                result = max(result, r-l+1)
        return result
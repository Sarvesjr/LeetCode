class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = res = nums[0]

        for i in range(1, len(nums)):
            prev = max(nums[i], prev + nums[i])
            res = max(res, prev)

        return res
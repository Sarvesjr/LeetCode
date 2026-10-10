class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum, rightSum = 0, sum(nums)
        for i, val in enumerate(nums):
            rightSum -= val
            if leftSum == rightSum:
                return i
            leftSum+= val
        return -1
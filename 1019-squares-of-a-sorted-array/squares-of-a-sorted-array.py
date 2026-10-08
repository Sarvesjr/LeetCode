class Solution(object):
    def sortedSquares(self, nums):
        """
        res = [0]*len(nums)
        l = 0
        r = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l]**2
                l+=1
            else:
                res[i] = nums[r]**2
                r-=1
        return res
        """
        return sorted(x*x for x in nums)
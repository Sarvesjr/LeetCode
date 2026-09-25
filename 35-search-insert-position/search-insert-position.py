class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while(l<=r):
            m=(l+r)//2
            
            if target==nums[m]:
                return m
            elif target < nums[m]:
                r = m-1
            else:
                l = m+1
        return l
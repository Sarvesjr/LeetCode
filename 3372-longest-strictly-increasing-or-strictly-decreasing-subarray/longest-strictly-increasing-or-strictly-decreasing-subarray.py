class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx = 1
        minn =1
        longest = 1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                maxx +=1
                
                minn=1
            elif nums[i]>nums[i+1]:
                minn +=1
                maxx =1
            else:
                maxx =1
                minn=1
            longest = max(minn,maxx,longest)
        return longest
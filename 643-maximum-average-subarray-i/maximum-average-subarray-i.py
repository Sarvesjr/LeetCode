class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        windowsum=0

        for i in range(k):
            windowsum+=nums[i]
            maxsum=windowsum
            
        for i in range(k,len(nums)):
            windowsum+=nums[i]
            windowsum-=nums[i-k]
            maxsum=max(windowsum,maxsum)
        return float (maxsum)/k
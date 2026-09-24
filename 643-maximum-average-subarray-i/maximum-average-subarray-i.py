class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        windowSum=0

        for i in range(k):
            windowSum+=nums[i]
            maxSum=windowSum
        
        for i in range(k,len(nums)):
            windowSum+=nums[i]
            windowSum-=nums[i-k]

            maxSum=max(windowSum,maxSum)
            
        return float(maxSum)/k
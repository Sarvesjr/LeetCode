class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minLen = float('inf')
        currSum = 0
        left = 0
        for right in range(len(nums)):
            currSum+=nums[right]
            while(currSum>=target):
                if(right-left+1) < minLen:
                    minLen = right-left+1
                currSum-= nums[left]
                left+=1
        return 0 if minLen == float('inf') else minLen
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxSum = 0
        windowSum = sum(nums[:k])
        freq = {}

        for i in range(k):
            freq[nums[i]] = freq.get(nums[i],0)+1

        if len(freq) == k:
            maxSum = windowSum

        for i in range(k, len(nums)):
            outgoing = nums[i-k]
            incoming = nums[i]

            freq[outgoing]-=1
            if freq[outgoing] == 0:
                del freq[outgoing]

            freq[incoming] = freq.get(incoming,0)+1

            windowSum = windowSum - outgoing + incoming

            if len(freq) == k:
                maxSum = max(maxSum, windowSum)
                
        return maxSum
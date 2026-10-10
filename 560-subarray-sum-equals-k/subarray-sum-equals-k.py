class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixSum = 0
        count = 0
        freq = {0:1}

        for num in nums:
            prefixSum += num
            if (prefixSum - k) in freq:
                count += freq[prefixSum - k]
            if prefixSum in freq:
                freq[prefixSum] += 1
            else:
                freq[prefixSum] = 1
        return count
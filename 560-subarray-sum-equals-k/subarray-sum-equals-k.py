class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count={0: 1}
        total,answer=0,0
        for num in nums:
            total+= num
            if total-k in count:
                answer += count[total-k]
            count[total] = count.get(total,0)+1
        return answer
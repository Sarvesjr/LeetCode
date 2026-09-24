class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen={0:1}
        total,answer=0,0

        for num in nums:
            total+=num
            req = total-k
            if req in seen:
                answer += seen[req]
            seen[total]=seen.get(total,0)+1
        return answer
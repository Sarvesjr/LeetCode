class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        prefix=0
        map={0:1}
        for x in nums:
            prefix+=x
            if prefix-k in map:
                count+=map[prefix-k]
            map[prefix]=map.get(prefix,0)+1
        return count
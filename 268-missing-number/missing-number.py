class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n*(n+1)//2 #get the total
        for num in nums:
            total-=num #keep subtracting the num from total, we will end up in the num which is absent
        return total
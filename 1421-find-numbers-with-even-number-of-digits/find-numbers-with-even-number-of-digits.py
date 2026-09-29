class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            digit = 0
            curr = nums[i]

            while curr>0:
                curr = curr/10
                digit+=1

            if digit%2==0:
                count+=1
        return count
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        n=len(nums)-1
        high=n
        while low<high:
            mid=low+(high-low)//2

            if nums[mid]<nums[high]:
                high=mid
            elif nums[mid]>nums[high] :
                low=mid+1
            else:
                high-=1

        return nums[low]
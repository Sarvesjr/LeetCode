class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low,mid,high=0,0,len(nums)-1
        while mid <= high:
            if nums[mid]==0: #put 0 in start
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1: #put 1 in middle(alr present due to prev iteration)
                mid+=1
            else: #put 2 in end
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
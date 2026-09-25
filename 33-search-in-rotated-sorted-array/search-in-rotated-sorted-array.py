class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start,end = 0, len(nums)-1
        #find mid element
        while(start<=end):
            mid = start+(end-start)//2

            if nums[mid]==target:
                return mid

            #check if left part is sorted
            if nums[mid]>=nums[start]:
                #check if target present in left part
                if target >= nums[start] and target < nums[mid]:
                    end = mid-1 #move left
                else:
                    start = mid+1 #move right
            #right part is sorted
            else:
                #check if target present in right part
                if target > nums[mid] and target <= nums[end]:
                    start = mid+1 #move right
                else:
                    end = mid-1 #move left
        return -1
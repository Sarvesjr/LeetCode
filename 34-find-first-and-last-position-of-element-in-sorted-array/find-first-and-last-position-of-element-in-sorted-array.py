class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findfirst():
            l=0
            r=len(nums)-1
            ans=-1
            while(l<=r):
                m=(l+r)//2

                if nums[m] == target:
                    ans=m
                    r=m-1 #search left
                elif nums[m]<target:
                    l = m+1
                else:
                    r = m-1
            return ans
            
        def findlast():
            l=0
            r=len(nums)-1
            ans=-1
            while(l<=r):
                m=(l+r)//2

                if nums[m] == target:
                    ans=m
                    l=m+1 #search right
                elif nums[m]<target:
                    l = m+1
                else:
                    r = m-1
            return ans
        return [findfirst(),findlast()]
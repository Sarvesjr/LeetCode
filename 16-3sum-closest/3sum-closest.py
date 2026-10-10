class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closestSum = float('inf')
        minDiff = float('inf')

        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1

            while left < right:
                currSum = nums[i]+nums[left]+nums[right]
                currDiff = abs(currSum - target)

                if currDiff < minDiff:
                    minDiff = currDiff
                    closestSum = currSum
                
                if currSum < target:
                    left+=1
                else:
                    right-=1

        return closestSum
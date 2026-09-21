class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i,j,cnt,maxi=0,0,0,0
        for j in range(len(nums)):
            if nums[j]==0:
                cnt+=1
            while(cnt>k):
                if nums[i]==0:
                    cnt-=1
                i+=1
            maxi=max(maxi,j-i+1)
        return maxi
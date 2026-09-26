class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.mergeSort(nums)
        return nums

        #Bubble sort O(n^2)
        """
        n=len(nums)
        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j]>nums[j-1]:
                    nums[j],nums[j-1]=nums[j-1],nums[j]
        return nums
        """

        #Insertion Sort O(n^2)
        """
        for i in range(1,len(nums)):
            for j in range(i,0,-1):
                if nums[j-1]>nums[j]:
                    nums[j-1],nums[j]=nums[j],nums[j-1]
                else:
                    break
        return nums
        """

        #Selection Sort O(n^2)
        """
        for i in range(len(nums)):
            mini=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[mini]:
                    mini=j
            nums[i],nums[mini]=nums[mini],nums[i]
        return nums
        """

    #Merge Sort O(n logn)
    def mergeSort(self, nums): 
        if len(nums) > 1: 
            mid = len(nums)//2
            L = nums[:mid] 
            R = nums[mid:] 

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1
        return nums
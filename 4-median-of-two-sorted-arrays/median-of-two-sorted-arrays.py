class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge both arrays
        nums1.extend(nums2)
        nums1.sort()
        
        n = len(nums1)
        mid = n // 2
        
        # If odd length, return middle element
        if n % 2 != 0:
            return nums1[mid]
        else:
            # If even length, return average of two middle elements
            return (nums1[mid - 1] + nums1[mid]) / 2.0

        
        
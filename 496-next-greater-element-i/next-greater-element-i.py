class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        stack = []

        for x in nums2:
            while stack and stack[-1] < x:
                value = stack.pop()
                map[value] = x
            stack.append(x)
        for i in range(len(nums1)):
            nums1[i] = map.get(nums1[i],-1)
        return nums1
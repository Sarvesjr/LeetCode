class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        res = 0
        for x in arr1:
            i = bisect.bisect_left(arr2, x - d)
            if i == len(arr2) or arr2[i] > x + d:
                res += 1
        return res
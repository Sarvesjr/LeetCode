class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        c = len(matrix[0])
        total = r*c
        left = 0
        right = total-1

        while left <= right:
            mid = left+(right-left)//2

            rp = mid//c
            cp = mid%c

            if matrix[rp][cp] < target:
                left = mid+1
            elif matrix[rp][cp] > target:
                right = mid-1
            else:
                return True
        return False
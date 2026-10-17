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
        lo = 0
        hi = total-1

        while lo <= hi:
            mid = lo+(hi-lo)//2
            
            rp = mid//c
            cp = mid%c

            if matrix[rp][cp] < target:
                lo = mid+1
            elif matrix[rp][cp] > target:
                hi = mid-1
            else:
                return True
        return False
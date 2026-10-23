# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = 0
        t = n
        while (t - h)>1:
            mid = (h+t)//2
            if isBadVersion(mid) == True:
                t = mid
            else:
                h = mid
        return t
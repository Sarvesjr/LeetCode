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
        l=1
        while l<n:
            m = l + (n-l)//2
            if isBadVersion(m):
                n=m
            else:
                l=m+1
        return l
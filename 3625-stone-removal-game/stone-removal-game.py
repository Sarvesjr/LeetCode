class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (0x61F03F807FC00 >> n & 1) == 1

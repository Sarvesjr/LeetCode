class Solution(object):
    def minChanges(self, s):
        return bin(int(s[::2], 2) ^ int(s[1::2], 2)).count("1")
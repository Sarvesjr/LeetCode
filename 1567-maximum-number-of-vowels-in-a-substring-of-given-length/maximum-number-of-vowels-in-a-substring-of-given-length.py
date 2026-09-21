class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels="aeiou"
        count,maxcount=0,0
        for i in range(len(s)):
            if s[i] in vowels:
                count+=1
            if i>=k:
                if s[i-k] in vowels:
                    count-=1
            maxcount=max(count,maxcount)
        return maxcount
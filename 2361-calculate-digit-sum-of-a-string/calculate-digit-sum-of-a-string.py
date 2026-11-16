class Solution(object):
    def curSum(self, s):
        curS = 0
        for c in s:
            curS += int(c)
        return str(curS)

    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while(len(s) > k):
            l = []
            # Divide
            i = 0
            while(i < len(s)):
                l.append(s[i:k + i])
                i += k
            
            # Replace & Merge
            s = ""
            for i in l:
                s += self.curSum(i)
        return s

                
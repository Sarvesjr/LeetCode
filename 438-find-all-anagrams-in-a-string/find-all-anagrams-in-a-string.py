class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need={}
        window={}
        result=[]

        #update need map
        for ch in p:
            need[ch]=need.get(ch,0)+1

        #update window map
        left=0
        for right in range(len(s)):
            ch=s[right]
            window[ch]=window.get(ch,0)+1
            
            #check window length exceeds condition then move right
            if right-left+1 > len(p):
                leftchar=s[left]
                window[leftchar]-=1
                if window[leftchar]==0:
                    del window[leftchar]
                left+=1

            #if matching then append left to result
            if window == need:
                result.append(left)

        return result
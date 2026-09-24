class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count={}
        left=0
        maxFreq=0
        result=0
        #add freqs to count
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1

            #find most frequent character
            maxFreq=max(maxFreq,count[s[right]])

            #update replacements to windowSize-maxFreq
            replacements=(right-left+1)-maxFreq

            #if replacements exceed k, move window left
            while replacements>k:
                count[s[left]]-=1
                left+=1
                replacements=(right-left+1)-maxFreq

            #save largest window and return
            result=max(result,right-left+1)
        return result
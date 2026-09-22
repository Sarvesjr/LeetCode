class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        mapP={}
        for i in range(len(p)):
            mapP[p[i]]=mapP.get(p[i],0)+1

        mapW={}

        result=[]
        left,right=0,0

        while(right<len(s)):
            mapW[s[right]]=mapW.get(s[right],0)+1
            #if window size exceeds p then remove left element and delete it
            if (right-left+1)>len(p):
                mapW[s[left]]-=1
                if mapW[s[left]]==0:
                    del mapW[s[left]]
                left+=1
            #if window matches p then find frequencies and append result
            if(right-left+1)==len(p):
                if mapP==mapW:
                    result.append(left)
            right+=1
        return result
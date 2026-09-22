class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False

        map1={}
        map2={}

        for ch in s1:
            map1[ch]=map1.get(ch,0)+1

        left=0
        right=0
        k=len(s1)

        while right < len(s2):
            map2[s2[right]]=map2.get(s2[right],0)+1

            if(right-left+1)>k:
                map2[s2[left]]-=1
                if map2[s2[left]]==0:
                    del map2[s2[left]]
                left+=1
            
            if(right-left+1)==k:
                if map1==map2:
                    return True
            right+=1
        return False
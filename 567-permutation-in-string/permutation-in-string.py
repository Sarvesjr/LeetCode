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

        #add map1
        for ch in s1:
            map1[ch]=map1.get(ch,0)+1

        left=0
        right=0
        k=len(s1)
        
        while right < len(s2):
            #add right character in map2:
            map2[s2[right]]=map2.get(s2[right],0)+1

            #if window size exceeds k:
            if(right-left+1)>k:
                map2[s2[left]]-=1 #removing left from freq map
                if map2[s2[left]]==0:
                    del map2[s2[left]] #removing character from map if freq 0
                left+=1
            
            #if window size equals k: check if both maps match:
            if(right-left+1)==k:
                if map1==map2:
                    return True
            right+=1
        return False
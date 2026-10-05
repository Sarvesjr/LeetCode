class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        og = num
        while(num!=0):
            digits=num%10
            if og%digits==0:
                count+=1
            num//=10
        return count
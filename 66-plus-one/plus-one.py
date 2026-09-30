class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i in range(len(digits)):
            number = number * 10 + digits[i]

        number+=1

        result=[]
        for ch in str(number):
            result.append(int(ch))

        return result
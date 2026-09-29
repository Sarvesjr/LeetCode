class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        product = 1
        """
        while n!=0:
            rem = n%10
            product *= rem
            sum += rem
            n/=10
        return product - sum
        """

        while n>0:
            product*=n%10
            sum+=n%10
            n/=10
        return product-sum
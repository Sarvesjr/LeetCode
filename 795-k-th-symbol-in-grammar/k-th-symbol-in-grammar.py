class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        same = True
        n = 2**(n-1)

        while n!=1:
            n//=2
            if k>n:
                k-=n
                same = not same
        return 0 if same else 1
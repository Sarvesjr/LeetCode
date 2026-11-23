class ProductOfNumbers(object):

    def __init__(self):
        self.prefix = [1]
        self.last_zero = 0

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.prefix.append(1)
            self.last_zero = len(self.prefix)-1
        else:
            self.prefix.append(self.prefix[-1]*num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        n = len(self.prefix) - 1
        if self.last_zero >= n - k + 1:
            return 0
        return self.prefix[n] // self.prefix[n - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
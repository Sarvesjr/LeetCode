class ProductOfNumbers(object):

    def __init__(self):
        self.li = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.li = [1]
        else:
            self.li.append(num*self.li[-1])
        return 
        if not self.li :
            if num == 0 :
                num = 1
                self.zero.add(0)
            self.li.append(num)
        elif num == 0 :
            self.zero.add(len(self.li))
            self.li.append(self.li[-1])
        else:
            if self.li[-1] == 0:
                self.li.append(num)
            else:
                self.li.append(num * self.li[-1])

        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.li):
            return 0
        return self.li[-1]//self.li[-k-1]
        n = len(self.li)
        ind = n - k - 1
        
        for i in self.zero :
            if i > ind :
                return 0
        if ind == -1 :
            return self.li[-1]
        return self.li[-1] // self.li[ind]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
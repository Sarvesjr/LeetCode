class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap={'(':')', '{':'}','[':']'}
        stack=[]

        for b in s:
            if b in hashmap:
                stack.append(b)
            else:
                if not stack:
                    return False

                popped = stack.pop()

                if hashmap[popped] != b :
                    return False

        return len(stack) == 0
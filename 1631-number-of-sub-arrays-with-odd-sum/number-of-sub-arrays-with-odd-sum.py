class Solution:
    def numOfSubarrays(self, arr):
        p = int(''.join('1' if x % 2 else '0' for x in arr), 2)
        s = 1
        while s < len(arr):
            p ^= p >> s
            s <<= 1
        odd = bin(p).count('1')
        return (odd * (len(arr) + 1 - odd)) % (10**9 + 7)
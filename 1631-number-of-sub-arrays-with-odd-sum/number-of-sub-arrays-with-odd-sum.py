class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        current_sum = 0
        total_count = 0
        even = 1
        odd = 0

        for i in arr:

            current_sum += i

            if current_sum % 2 != 0:
                odd += 1
                total_count += even 
            
            else:
                even += 1
                total_count += odd
        
        return total_count % (10**9 + 7)
        
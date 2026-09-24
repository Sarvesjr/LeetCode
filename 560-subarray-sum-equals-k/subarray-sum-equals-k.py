class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count={0: 1}
        curr_prefix,answer=0,0
        for num in nums: #take each number
            curr_prefix += num #update current prefix sum

            if curr_prefix-k in count: #check if we have already seen the reuired previous sum
                answer += count[curr_prefix-k] #add how many times we saw it

            count[curr_prefix] = count.get(curr_prefix,0)+1 #update the sum
        return answer
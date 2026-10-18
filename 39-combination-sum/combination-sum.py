class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(target, combination, start):
            if target == 0:
                result.append(list(combination))
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(target - candidates[i], combination, i)
                combination.pop()

        backtrack(target, [], 0)
        return result
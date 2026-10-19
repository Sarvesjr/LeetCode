
class Solution:
    def solve(self, digit, output, i, ans, mapping):
        if i >= len(digit):
            ans.append("".join(output))
            return
        num = int(digit[i])
        value = mapping[num]
        for j in range(len(value)):
            output.append(value[j])
            self.solve(digit, output, i + 1, ans, mapping)
            output.pop()

    def letterCombinations(self, digits):
        ans = []
        if not digits:
            return ans
        mapping = ["", "", "abc", "def", "ghi", "jkl",
                   "mno", "pqrs", "tuv", "wxyz"]

        self.solve(digits, [], 0, ans, mapping)
        return ans

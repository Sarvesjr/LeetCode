class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        INF = 10000

        memo = [[-1] * (k + 1) for _ in range(n + 1)]
        cost = [[INF] * (n + 1) for _ in range(n + 1)]

        # Precompute minimum changes for every substring
        for d in range(1, n // 2 + 1):
            tmp = [[0] * (n + 1) for _ in range(n + 1)]

            for length in range(2 * d, n + 1, d):
                for idx in range(n - length + 1):
                    ops = 0

                    for o in range(d):
                        if s[idx + o] != s[idx + length - d + o]:
                            ops += 1

                    tmp[idx][length] = (
                        ops + tmp[idx + d][length - 2 * d]
                    )

                    cost[idx][length] = min(
                        cost[idx][length],
                        tmp[idx][length]
                    )

        # Recursive DP with memoization
        def solve(idx, k):
            if idx == n or k == 0:
                return 0 if idx == n and k == 0 else INF

            if memo[idx][k] != -1:
                return memo[idx][k]

            res = INF

            for length in range(2, n - idx + 1):
                res = min(
                    res,
                    cost[idx][length] + solve(idx + length, k - 1)
                )

            memo[idx][k] = res
            return res

        return solve(0, k)
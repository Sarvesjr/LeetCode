class Solution(object):
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        ans = [envelopes[0][1]]

        for i in range(1, len(envelopes)):
            height = envelopes[i][1]

            if height > ans[-1]:
                ans.append(height)
            else:
                index = bisect_left(ans, height)
                ans[index] = height

        return len(ans)
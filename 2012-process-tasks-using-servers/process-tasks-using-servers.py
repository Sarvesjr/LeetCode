from heapq import heapify, heappush, heappop
class Solution(object):
    def assignTasks(self, servers, tasks):
        free = [(w, i) for i, w in enumerate(servers)]
        heapify(free)
        ans = []
        busy = []
        for s, t in enumerate(tasks):
            while busy and busy[0][0] <= s:
                x = heappop(busy)
                heappush(free, (x[1], x[2]))
            if free:
                w, i = heappop(free)
                start = s
            else:
                start, w, i = heappop(busy)
            heappush(busy, (start + t, w, i))
            ans.append(i)
        return ans
from heapq import heappush, heappop
from collections import Counter

class Solution(object):
    def busiestServers(self, k, arrival, load):
        free = list(range(k))
        handled = []
        busy = []

        for i, (t, d) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                end, server = heappop(busy)
                heappush(free, i + (server - i) % k)

            if free:
                x = heappop(free) % k
                heappush(busy, (t + d, x))
                handled.append(x)

        counts = Counter(handled)
        maximum = max(counts.values())

        return [server for server in range(k)
                if counts[server] == maximum]
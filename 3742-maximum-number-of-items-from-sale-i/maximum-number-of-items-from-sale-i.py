class Solution(object):
    def maximumSaleItems(self, items, budget):
        factors = [item[0] for item in items]
        prices = [item[1] for item in items]
        have = [0] * (max(factors) + 1)
        for f in factors:
            have[f] += 1
        gains = {}
        for factor in set(factors):
            gains[factor] = sum(have[factor::factor])
        cheapest = min(prices)
        best = [i // cheapest for i in range(budget + 1)]
        for factor, price in items:
            gain = gains[factor]

            if gain > price // cheapest:
                for b in range(budget, price - 1, -1):
                    best[b] = max(best[b], best[b - price] + gain)
        return best[budget]
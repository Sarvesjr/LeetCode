
class Solution(object):
    def maximumSaleItems(self, items, budget):
        factors = [item[0] for item in items]
        prices = [item[1] for item in items]

        have = [0] * (max(factors) + 1)

        for f in factors:
            have[f] += 1

        def deals(factor):
            count = 0
            for f in range(factor, len(have), factor):
                count += have[f]
            return count - 1

        cheapest = min(prices)

        order = sorted(
            range(len(prices)),
            key=lambda i: prices[i]
        )

        copies = 0

        for i in order:
            price = prices[i]
            factor = factors[i]

            if price >= 2 * cheapest:
                break

            if price > budget:
                break

            pairs = min(deals(factor), budget // price)

            copies += 2 * pairs
            budget -= pairs * price

        return copies + budget // cheapest

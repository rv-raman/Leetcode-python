class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = 10001
        profit = 0
        n = len(prices)
        for i in range(n):
            if mn > prices[i]:
                mn = prices[i]
            elif profit < prices[i] - mn:
                profit = prices[i] - mn
        return profit

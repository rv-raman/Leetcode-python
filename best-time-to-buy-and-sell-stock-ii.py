class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        if n == 0:
            return profit
        for i in range(n - 1):
            if prices[i + 1] > prices[i]:
                profit += (prices[i + 1] - prices[i])
        return profit



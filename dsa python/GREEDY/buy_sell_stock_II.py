class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            # If tomorrow's price is higher, take the profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
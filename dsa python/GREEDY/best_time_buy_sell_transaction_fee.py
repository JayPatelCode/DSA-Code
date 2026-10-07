class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        profit = 0
        buy = prices[0]

        for price in prices:
            if price < buy:
                buy = price

            elif price > buy + fee:
                profit += price - buy - fee
                buy = price - fee

        return profit
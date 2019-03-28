class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            current_price = prices[i]
            profit = current_price - min_price

            max_profit = max(max_profit, profit)

            min_price = min(current_price, min_price)
        return max_profit

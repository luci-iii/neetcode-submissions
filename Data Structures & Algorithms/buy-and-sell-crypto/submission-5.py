class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        min_price = float('inf')
        max_profit = 0

        for n in prices:
            if min_price > n:
                min_price = n

            profit = n - min_price

            if profit > max_profit:
                max_profit = profit      



        return max_profit
#Best time to buy and sell stock / maxSumSubArray
class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        finalProfit,currProfit = 0,0
        for i,price in enumerate(prices[1:]):
            currProfit = max(currProfit + (price - prices[i]), 0) #reset to 0 if dips below 0
            finalProfit = max(currProfit,finalProfit)
        return(finalProfit)

    # Non Kadane solution 
    # def maxProfit(self, prices: List[int]) -> int:
    #     buy_price, max_profit = None, 0
    #     for price in prices:
    #         if buy_price is None:
    #             buy_price = price
    #         elif price < buy_price:
    #             buy_price = price
    #         else:
    #             max_profit = max(max_profit, price - buy_price)
    #     return max_profit
    

print(Solution().maxProfit([7,1,5,3,6,4]))
#5
# 7 -6 4 -2 3 -2
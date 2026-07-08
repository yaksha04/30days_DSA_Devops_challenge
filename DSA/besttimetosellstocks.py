class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        profit=0
        for i in range(1,len(prices)):
            current_price=prices[i]-min_price
            if current_price>profit:
                profit=current_price
            min_price=min(min_price,prices[i])    
        return profit    

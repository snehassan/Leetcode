class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        first_buy = -float('inf')
        first_sell = 0
        second_buy = -float('inf')
        second_sell = 0
        
        for p in prices:

            first_buy = max(first_buy, -p)

            first_sell = max(first_sell, first_buy + p)
            second_buy = max(second_buy, first_sell - p)
            second_sell = max(second_sell, second_buy + p)
            
        return second_sell
        
            
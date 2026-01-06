class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        best = 0
        for i in prices:
            minp = min(minp,i)
            best = max(best, i-minp)
        return best

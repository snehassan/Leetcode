from functools import lru_cache
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        price_map = {(h,w): p for h,w,p in prices}

        @lru_cache(None)

        def dp(h,w):
            res = price_map.get((h,w),0)

            for i in range(1, h//2 + 1):
                res = max(res, dp(i,w) + dp(h-i,w))
            for j in range(1, w//2+1):
                res = max(res,dp(h,j)+dp(h,w-j))
            return res
        return dp(m,n)
class Solution:
    
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @functools.lru_cache(None)
        def func(i, k):
            if k == 0 or i == len(piles): return 0
            res, cur = func(i + 1, k), 0
            for j in range(min(len(piles[i]), k)):
                cur += piles[i][j]
                res = max(res, cur + func(i+1, k-j-1))
            return res
        
        return func(0, k)
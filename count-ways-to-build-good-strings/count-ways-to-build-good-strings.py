from functools import lru_cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        @lru_cache(maxsize=32)
        def rec(patt):
            
            if low <= patt <= high:
                return rec(patt + zero) + rec(patt + one) + 1
            if patt > high:
                return 0
            return rec(patt + zero) + rec(patt + one)
        
        return rec(0) % (int(1e9) + 7)
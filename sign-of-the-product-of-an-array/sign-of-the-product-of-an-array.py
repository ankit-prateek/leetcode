class Solution:
    def arraySign(self, nums: List[int]) -> int:
        a=1
        for i in nums:
            a*=i
        if a==0:
            return a
        return 1 if a>1 else -1
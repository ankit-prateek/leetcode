from bisect import bisect
class Solution:
    def numSubseq(self, nums: List[int], tar: int) -> int:
        ans=0
        n=len(nums)
        nums.sort()
        for i in range(n):
            x=tar-nums[i]
            a=bisect(nums,x)
            if a>i:
                t=(a-i)-1
                ans+=2**t
        return ans%(10**9+7)

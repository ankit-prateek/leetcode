class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        ans=[]
        while i<n:
            a=nums[i]
            b=nums[i+1]
            i+=2
            ans.extend([b]*a)
        return ans

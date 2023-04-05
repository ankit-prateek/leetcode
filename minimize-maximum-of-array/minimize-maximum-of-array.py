from math import ceil
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s=sum(nums)
        n=len(nums)
        left=0
        for i in range(n-1,-1,-1):
            avg=ceil(s/n)
            if nums[i]>avg:
                left+=nums[i]-avg
                nums[i]=avg
            else:
                x=avg-nums[i]
                if x<=left:
                    left-=x
                    nums[i]+=x
                else:
                    nums[i]+=left
                    left=0
                
            n-=1
            s-=nums[i]
        return max(nums)
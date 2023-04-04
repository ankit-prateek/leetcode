class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        t=[]
        i=0
        j=len(nums)-1
        while i<=j:
            if abs(nums[i])>abs(nums[j]):
                t.append(nums[i]*nums[i])
                i+=1
            else:
                t.append(nums[j]*nums[j])
                j-=1
        return t[::-1]
        
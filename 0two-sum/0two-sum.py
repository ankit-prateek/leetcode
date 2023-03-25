class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(0,len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        for i,j in d.items():
            b=target-i
            if b in d :
                if i!=b:
                    return [j[0],d[b][0]]
                if len(j)>1:
                    return j[:2]
        
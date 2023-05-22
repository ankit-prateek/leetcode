class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        x=[[j,i] for i,j in d.items()]
        x.sort(reverse=True)
        return list(map(lambda t:t[1],x[:k]))
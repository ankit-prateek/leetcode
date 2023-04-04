class Solution:
    def partitionString(self, s: str) -> int:
        d=set()
        ans=1
        for i in s:
            if i in d:
                d=set([i])
                ans+=1
            else:
                d.add(i)
        return ans

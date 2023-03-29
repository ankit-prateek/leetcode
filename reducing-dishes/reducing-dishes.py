class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        s=sum(sat)
        ans=0
        sat.sort()
        t=1
        for i in sat:
            ans+=t*i
            t+=1
        imax=ans
        for i in sat:
            ans-=s
            s-=i
            imax=max(imax,ans)
        return imax
        






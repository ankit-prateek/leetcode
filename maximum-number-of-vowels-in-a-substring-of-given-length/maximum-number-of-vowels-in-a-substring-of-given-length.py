class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        x="aeiou"
        n=len(s)
        ans=0
        for i in range(min(n,k)):
            if s[i] in x:
                ans+=1
        imax=ans
        for i in range(k,n):
            if s[i] in x:
                ans+=1
            if s[i-k] in x:
                ans-=1
            imax=max(imax,ans)
        return imax
            
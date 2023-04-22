class Solution(object):
    @functools.lru_cache(None)
    def check(self,i,j):
        if i>=0 and i<self.n and j>=0 and j<self.m:
            if self.a[i]==self.b[j]:
                return self.check(i+1,j+1)+1
            else:
                a=self.check(i+1,j)
                b=self.check(i,j+1)
                return max(a,b)
        return 0
    def longestPalindromeSubseq(self, s):
        self.a=s
        self.b=s[::-1]
        self.n=len(s)
        self.m=len(s)
        return self.check(0,0)
                

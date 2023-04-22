class Solution:
    @functools.lru_cache(None)
    def check(self,i,j):
        if  i<self.n and j<self.n:
            if self.a[i]==self.b[j]:
                return self.check(i+1,j+1)+1
            else:
                a=self.check(i+1,j)
                b=self.check(i,j+1)
                return max(a,b)
        return 0
    def minInsertions(self, s: str) -> int:
        self.a=s
        self.b=s[::-1]
        self.n=len(s)
        x=self.check(0,0)
        return self.n-x
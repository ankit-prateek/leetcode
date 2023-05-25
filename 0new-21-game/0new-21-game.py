class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if N<K:
            return 0.0
        dp=[0]*(N+W)
        for i in range(K,N+1):
            dp[i]=1
        density=1/float(W)
        tmp=sum(dp[K:K+W])
        for i in range(K-1,-1,-1):
            dp[i]=tmp*density
            tmp+=dp[i]-dp[i+W]
        return dp[0]
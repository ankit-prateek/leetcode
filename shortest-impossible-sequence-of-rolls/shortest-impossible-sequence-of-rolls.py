class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        d={i:0 for i in range(1,k+1)}
        i=0
        n=len(rolls)
        t=0
        while i<n:
            ans=k
            while i<n and ans!=0:
                if d[rolls[i]]==t:
                    ans-=1
                    d[rolls[i]]+=1
                i+=1
            if i==n and ans==0:
                t+=1
            t+=1
        print(d)
        return t
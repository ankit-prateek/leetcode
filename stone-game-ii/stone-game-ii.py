class Solution:
    def stoneGameII(self, piles: List[int]) -> int:      
        length=len(piles)
        mem=[[None]*(2*length) for _ in range(length)]
        
        def Helper(i,M):
            if i>=length:
                return 0
            if mem[i][M] is not None:
                return mem[i][M]
            result=float('-inf')
            sums=0
            for k in range(1,2*M+1):             
                if i+k<=length:
                    sums+=piles[i+k-1]
                    result=max(result,sums-Helper(i+k,max(M,k)))
                else:
                    break
            mem[i][M]=result
            return result
            
        return (Helper(0,1)+sum(piles))//2
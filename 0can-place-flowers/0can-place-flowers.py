class Solution:
    def canPlaceFlowers(self, bed: List[int], t: int) -> bool:
        n=len(bed)
        for i,x in enumerate(bed):
            if x==0:
                if i+1<n and bed[i+1]==0:
                    if i==0 or bed[i-1]==0:
                        bed[i]=1
                        t-=1
                elif i+1==n and bed[i-1]==0:
                    bed[i]=1
                    t-=1
        #print(bed)
        return t<=0


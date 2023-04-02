class Solution:
    def bisect(self,a,ele, x):
        lo,hi = 0,len(a)
        while lo < hi:
            mid = (lo+hi)//2
            if ele*a[mid] < x: lo = mid+1
            else: hi = mid
        return lo
    def successfulPairs(self, spells: List[int], potions: List[int], s: int) -> List[int]:
        potions.sort()
        n=len(spells)
        m=len(potions)
        for i in range(n):
            x=self.bisect(potions,spells[i],s)
            spells[i]=m-x
        return spells


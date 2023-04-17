class Solution:
    def kidsWithCandies(self, c: List[int], ex: int) -> List[bool]:
        x=max(c)
        for i in range(len(c)):
            c[i]=c[i]+ex>=x
        return c
                
        
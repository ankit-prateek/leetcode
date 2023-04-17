class Solution:
    def kidsWithCandies(self, c: List[int], ex: int) -> List[bool]:
        x=max(c)
        return [i+ex>=x for i in c]
        
        
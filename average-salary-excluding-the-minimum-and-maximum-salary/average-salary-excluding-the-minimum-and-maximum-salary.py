class Solution:
    def average(self, sal: List[int]) -> float:
        sal.sort()
        x=sum(sal[1:-1])/(len(sal)-2)
        return x
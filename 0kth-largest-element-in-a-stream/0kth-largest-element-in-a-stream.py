from bisect import insort
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.ans=sorted(nums)
        
        

    def add(self, val: int) -> int:
        insort(self.ans,val)
        
        return self.ans[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
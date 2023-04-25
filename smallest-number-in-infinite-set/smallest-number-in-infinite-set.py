from bisect import insort
class SmallestInfiniteSet:

    def __init__(self):
        self.d=1
        self.add=[]
        

    def popSmallest(self) -> int:
        if self.add:
            if self.d>(-1*self.add[-1]):
                return -1*self.add.pop()
        self.d+=1
        return self.d-1

        

    def addBack(self, num: int) -> None:
        if self.d>num and -1*num not in self.add:
            insort(self.add,-1*num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
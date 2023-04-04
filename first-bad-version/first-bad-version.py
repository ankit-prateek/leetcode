# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i=0
        while i<n:
            mid=(i+n)//2
            if isBadVersion(mid):
                n=mid
            else:
                i=mid+1
        return i
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=set()
        ax=set(nums1)
        b=set()
        bx=set(nums2)
        for i in nums1:
            if i not in bx and i not in a:
                a.add(i)
        for i in nums2:
            if i not in ax and i not in b:
                b.add(i)
        return [list(a),list(b)]

from bisect import insort
class Solution:
    def lastStoneWeight(self, st: List[int]) -> int:
        n=len(st)
        st.sort()
        while n>1:
            a=st.pop()
            b=st.pop()
            n-=2
            if a!=b:
                insort(st,a-b)
                n+=1
            print(st)
        return 0 if len(st)==0 else st[0]
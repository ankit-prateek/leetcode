class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i,j=0,0
        st=[]
        n=len(pushed)
        while i<n and j<n:
            if st and st[-1]==popped[j]:
                st.pop()
                j+=1
            else:
                st.append(pushed[i])
                i+=1
        #print(st,j)
        while j<n:
            if st:
                x=st.pop()
                #print(x,popped[j])
                if x!=popped[j]:
                    return False
            j+=1
        return False if st else True


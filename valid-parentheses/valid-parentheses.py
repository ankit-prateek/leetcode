class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={
            "}":"{",
            "]":"[",
            ")":"("
        }
        for i in s:
            if i in "([{":
                st.append(i)
            else:
                if st:
                    x=st.pop()
                    if d[i]!=x:
                        return False
                else:
                    return False
        return True if len(st)==0 else False 
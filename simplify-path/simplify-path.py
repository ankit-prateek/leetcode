class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        s=path.split("/")
        s=list(filter(lambda x:(x!="" and x!="."),s))
        i=0
        n=len(s)
        while i<n:
            if s[i]=="..":
                if st:
                    st.pop()
            else:
                st.append(s[i])
            i+=1
            
        return "/"+"/".join(st)
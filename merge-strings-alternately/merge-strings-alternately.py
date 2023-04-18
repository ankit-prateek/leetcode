class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        n,m=len(word1),len(word2)
        ans=[]
        while i<n and j<m:
            ans.append(word1[i])
            ans.append(word2[j])
            i+=1
            j+=1
        while i<n:
            ans.append(word1[i])
            i+=1
        while j<m:
            ans.append(word2[j])
            j+=1
        return "".join(ans)
        
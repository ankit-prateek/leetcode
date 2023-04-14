class Solution(object):
    def longestPalindromeSubseq(self, s):
        n=len(s)
        mat=[[0]*(n) for i in range(n)]
        for i in range(n-1,-1,-1):
            mat[i][i]=1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    mat[i][j]=mat[i+1][j-1]+2
                else:
                    mat[i][j]=max(mat[i+1][j],mat[i][j-1])
        return mat[0][-1]
                

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n,m=len(mat),len(mat[0])
        i=0
        j=0
        ans=0
        k=len(mat[0])-1
        while i<n and j<m and k>=0:
            if k!=j:
                ans+=mat[i][j]
            ans+=mat[i][k]
            i+=1
            j+=1
            k-=1
        return ans
        
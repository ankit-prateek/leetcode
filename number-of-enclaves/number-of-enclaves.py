class Solution:
    def check(self,grid,i,j):
        n=len(grid)
        m=len(grid[0])
        grid[i][j]=2
        que=[[i,j]]
        lo,hi=0,1
        while lo<hi:
            i,j=que[lo]
            #print(que)
            lo+=1
            if i+1<n and grid[i+1][j]==1:
                grid[i+1][j]=2
                que.append([i+1,j])
                hi+=1
            if i-1>=0 and grid[i-1][j]==1:
                grid[i-1][j]=2
                que.append([i-1,j])
                hi+=1
            if j+1<m and grid[i][j+1]==1:
                grid[i][j+1]=2
                que.append([i,j+1])
                hi+=1
            if j-1>=0 and grid[i][j-1]==1:
                grid[i][j-1]=2
                que.append([i,j-1])
                hi+=1
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        ans=0
        for j in range(m):
            if grid[0][j]==1:
                self.check(grid,0,j)
                #print(0,j,grid) 
            if grid[n-1][j]==1:
                self.check(grid,n-1,j)
                #print(n-1,j,grid)
        for i in range(n):
            if grid[i][0]==1:
                self.check(grid,i,0)
                #print(i,0,grid)
            if grid[i][m-1]==1:
                self.check(grid,i,m-1)
                #print(i,m-1,grid)
        #print(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    ans+=1
        return ans
            
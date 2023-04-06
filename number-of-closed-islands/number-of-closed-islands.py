class Solution:
    def check(self,grid,i,j):
        n=len(grid)
        m=len(grid[0])
        que=[[i,j]]
        lo,hi=0,1
        ans=True
        while lo<hi:
            i,j=que[lo]
            #print(que)
            grid[i][j]=2
            lo+=1
            if i+1>=n or i-1<0 or j+1>=m or j-1<0:
                #print("worng",i,j)
                ans=False
                
            if i+1<n and grid[i+1][j]==0:
                que.append([i+1,j])
                hi+=1
            if i-1>=0 and grid[i-1][j]==0:
                que.append([i-1,j])
                hi+=1
            if j+1<m and grid[i][j+1]==0:
                que.append([i,j+1])
                hi+=1
            if j-1>=0 and grid[i][j-1]==0:
                que.append([i,j-1])
                hi+=1
        return ans



    def closedIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=0   
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    #print(i,j)
                    if self.check(grid,i,j):
                        #print("true",i,j)
                        ans+=1
        return ans
                    

        
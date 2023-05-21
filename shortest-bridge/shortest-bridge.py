class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        N = len(A)
        M = len(A[0])
        islands = collections.defaultdict(list)
                
        def neighbors(r, c):
            for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nr = r + d[0]
                nc = c + d[1]
                if 0 <= nr < N and 0 <= nc < M:
                    yield nr, nc
        
        def buildIsland(r, c, index):
            if A[r][c] == 1:
                A[r][c] = index
                count = 0
                for nr, nc in neighbors(r, c):
                    buildIsland(nr, nc, index)
                    if A[nr][nc] == index:
                        count += 1
                if count != 4:
                    islands[index].append((r, c))
        
        index = 2
        for i in range(N):
            for j in range(M):
                if A[i][j] == 1:
                    buildIsland(i, j, index)
                    index += 1   
                    
        minDist = float("inf")
        for (r1, c1) in islands[2]:
            for (r2, c2) in islands[3]:
                dist = abs(r1 - r2) + abs(c1 - c2) - 1
                minDist = min(minDist, dist)
        return minDist
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def find(x):
            while x in uf:
                while uf[x] in uf:
                    uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False
            uf[px] = py
            return True

        edgeList.sort(key=lambda x: x[2])
        i, res, uf = 0, [False]*len(queries), {}
        for limit,x,y,idx in sorted((q[2],q[0],q[1],i) for i,q in enumerate(queries)):
            while i<len(edgeList) and edgeList[i][2]<limit:
                union(edgeList[i][0],edgeList[i][1])
                i+=1
            res[idx] = (find(x)==find(y))
        return res
from collections import defaultdict

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges = [(t, u-1, v-1) for t,u,v in edges]
        
        common = []
        arr = []
        brr = []
        
        for t, u, v in edges:
            if t == 1:
                arr.append((u,v))
            if t == 2:
                brr.append((u,v))
            if t == 3:
                common.append((u,v))
        
        def traverse(graph, specific=False):
            sizes = []
            visited = [False for _ in range(n)]
            
            for i in range(n):
                if visited[i] or not d[i]:
                    continue
                size = 1
                stack = [i]
                visited[i] = True
                while stack:
                    cur = stack.pop()
                    for nex in d[cur]:
                        if visited[nex]:
                            continue
                        visited[nex] = True
                        stack.append(nex)
                        size += 1
                sizes.append(size)
                if specific:
                    break
                
            return sizes, all(visited)
        
        ################################################
        
        d = defaultdict(list)
        for u,v in common:
            d[u].append(v)
            d[v].append(u)
        
        sizes, _ = traverse(d)
        
        ################################################
        
        d = defaultdict(list)
        for u,v in common:
            d[u].append(v)
            d[v].append(u)
        
        for u,v in arr:
            d[u].append(v)
            d[v].append(u)
        
        _, all_visited_a = traverse(d, specific=True)
        
        ################################################
        
        d = defaultdict(list)
        for u,v in common:
            d[u].append(v)
            d[v].append(u)
        
        for u,v in brr:
            d[u].append(v)
            d[v].append(u)
        
        _, all_visited_b = traverse(d, specific=True)
        
        ################################################
        
        if not(all_visited_a and all_visited_b):
            return -1
        
        expected_commons = sum(x-1 for x in sizes)
        res = len(common) - expected_commons
        
        expected_specific = n - expected_commons - 1
        res += len(arr) + len(brr) - 2*expected_specific
        
        return res
        
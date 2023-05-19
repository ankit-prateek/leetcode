from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors, q = {}, deque()
        
        for i in range(len(graph)):
            if i in colors: 
                continue
                
            q.append((i, 1))
            while q:
                node, color = q.popleft()

                if node in colors:
                    if colors[node] != color:
                        return False
                else:
                    colors[node] = color
                    q.extend([(x, color ^ 1) for x in graph[node]])
        
        return True
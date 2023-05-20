class Solution(object):
    def calcEquation(self, equations, values, queries):
        edges, nodes, connected = {}, set(), collections.defaultdict(set)
        for equation, value in zip(equations, values):
            if equation[0] == equation[1]: continue
            edges[(equation[0], equation[1])] = value
            edges[(equation[1], equation[0])] = 1.0/value
            nodes.add(equation[0])
            nodes.add(equation[1])
            connected[equation[0]].add(equation[1])
            connected[equation[1]].add(equation[0])
        
        def dfs(n1, n2, visited, val):
            if n2 in connected[n1]:
                self.val = val * edges[(n1, n2)]
                return
            for n in connected[n1]:
                if n not in visited:
                    visited[n] = True
                    dfs(n, n2, visited, val * edges[(n1, n)])
                    del visited[n]
            return
    
        def calcEach(n1, n2):
            if n1 not in nodes or n2 not in nodes:
                return -1.0
            visited = {}
            self.val = -1.0
            dfs(n1, n2, visited, 1)
            return self.val
                
        return [ calcEach(query[0], query[1]) for query in queries ]
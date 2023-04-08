"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def clone(self,node,d):
        que=[node]
        i,n=0,1
        vis=set()
        while i<n:
            node=que[i]
            i+=1
            if node not in vis:
                vis.add(node)
                ne=[]
                for x in node.neighbors:
                    ne.append(d[x])
                    que.append(x)
                    n+=1
                d[node].neighbors=ne
        


    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return
        d={}
        que=[node]
        ans=node
        i,n=0,1
        while i<n:
            node=que[i]
            i+=1
            if node not in d:
                d[node]=Node(node.val)
                for x in node.neighbors:
                    que.append(x)
                    n+=1
        self.clone(node,d)
        return d[ans]



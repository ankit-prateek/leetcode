# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        root.n=""
        root.ans=0
        que=[root]
        i,n=0,1
        while i<n:
            root=que[i]
            i+=1
            if root.left:
                if root.n=="l":
                    root.left.ans=1
                else:
                    root.left.ans=root.ans+1
                root.left.n="l"
                que.append(root.left)
                n+=1
            if root.right:
                if root.n=="r":
                    root.right.ans=1
                else:
                    root.right.ans=root.ans+1
                root.right.n="r"
                que.append(root.right)
                n+=1
        x=0
        for i in que:
            x=max(x,i.ans)
        return x
        return max(que,lambda s:s.ans)
        return 1
            
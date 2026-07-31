# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res=[root.val]
        def DFS(root):
            leftMax=0
            rightMax=0
            if root.left:
                leftMax=DFS(root.left)
            if root.right:
                rightMax=DFS(root.right)
            leftMax=max(leftMax,0)
            rightMax=max(rightMax,0)
            res[0]=max(res[0],root.val+leftMax+rightMax)
            return root.val+max(leftMax,rightMax)
        DFS(root)
        return res[0]
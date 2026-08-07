# Definition for a binary tree node.
# class TreeNode:
# def __init__(self, val=0, left=None, right=None):
# self.val = val
# self.left = left
# self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = 0

        def inorder(node):
            if not node:
                return

            inorder(node.left) # go left first - smaller elements

            self.count += 1
            if self.count == k: # found kth
                self.ans = node.val
                return

            inorder(node.right) # go right

        inorder(root)
        return self.ans
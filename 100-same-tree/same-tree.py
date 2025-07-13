# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        # If both are empty, they are the same
        if p is None and q is None:
            return True
        # If exactly one is empty, they differ
        if p is None or q is None:
            return False
        # Values must match, and sub‑trees must match
        return (
            p.val == q.val and
            self.isSameTree(p.left,  q.left) and
            self.isSameTree(p.right, q.right)
        )
        
        
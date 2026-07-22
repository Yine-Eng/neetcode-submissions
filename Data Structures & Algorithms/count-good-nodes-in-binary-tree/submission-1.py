# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, maximum):
            if node is None:
                return 0
            if node.val >= maximum:
                return 1 + helper(node.left, max(maximum, node.val)) + helper(node.right, max(maximum, node.val))
            else:
                return helper(node.left, max(maximum, node.val)) + helper(node.right, max(maximum, node.val))
        return helper(root, root.val)
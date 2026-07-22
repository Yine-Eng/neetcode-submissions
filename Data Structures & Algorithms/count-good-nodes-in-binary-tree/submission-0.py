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
                maximum = node.val
                return 1 + helper(node.left, maximum) + helper(node.right, maximum)
            else:
                return helper(node.left, maximum) + helper(node.right, maximum)
        return helper(root, root.val)
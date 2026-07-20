# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(node, subRoot):
            if (node and subRoot is None) or (node is None and subRoot):
                return False
            if node is None and subRoot is None:
                return True
            if node.val != subRoot.val:
                return False
            if node.val == subRoot.val:
                return helper(node.left, subRoot.left) and helper(node.right, subRoot.right)

        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                answer = helper(node, subRoot)
                if answer:
                    return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False
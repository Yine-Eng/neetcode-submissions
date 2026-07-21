# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root is None:
            return output
        queue = deque([root])

        while queue:

            for i in range(len(queue)):
                current = queue.popleft()
                if i == 0:
                    rightmost = current.val
                if current.right:
                    queue.append(current.right)
                if current.left:
                    queue.append(current.left)
                
            output.append(rightmost)

        return output
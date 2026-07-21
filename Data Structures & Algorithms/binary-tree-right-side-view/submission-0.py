# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels, output = [], []
        if root is None:
            return output
        queue = deque([root])

        while queue:
            level = []

            for i in range(len(queue)):
                current = queue.popleft()
                level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            levels.append(level)

        for level in levels:
            output.append(level[-1])
        return output
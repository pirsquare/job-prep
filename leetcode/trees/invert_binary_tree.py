from collections import deque

# You are given the root of a binary tree root. Invert the binary tree and return its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#================================
# dfs_recursive 1
#================================
def dfs_recursive(node):
    right = node.right
    left = node.left

    node.left = right
    node.right = left

    for next_node in [node.left, node.right]:
        if next_node:
            dfs_recursive(next_node)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        dfs_recursive(root)
        return root


#================================
# dfs_recursive 2
#================================
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


#================================
# dfs iterative
#================================
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


#================================
# bfs
#================================
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        visited = set()
        queue = deque()

        visited.add(root)
        queue.append(root)

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            for neighbor in [node.left, node.right]:
                if neighbor and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return root

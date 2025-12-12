

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # Reference to the left child
        self.right = None # Reference to the right child

# Example of creating a simple binary tree:
root = TreeNode("Root")
node_a = TreeNode("A")
node_b = TreeNode("B")

root.left = node_a
root.right = node_b

# Accessing value:
print(root.value)       # Output: Root
print(root.left.value)  # Output: A
print(root.right.value) # Output: B

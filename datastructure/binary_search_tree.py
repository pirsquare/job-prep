


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    """Inserts a new key into the BST."""
    if root is None:
        return Node(key)

    if root.val > key:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    # Handle duplicates if needed; this example ignores them
    return root

def search(root, key):
    """Searches for a key in the BST."""
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root is not None # Returns True if found, False otherwise

    # Key is smaller than root's key
    if root.val > key:
        return search(root.left, key)
    # Key is greater than root's key
    return search(root.right, key)

# Example Usage:
root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Search for 40:", search(root, 40)) # Output: Search for 40: True
print("Search for 90:", search(root, 90)) # Output: Search for 90: False

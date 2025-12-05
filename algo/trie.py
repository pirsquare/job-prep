
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # True if this node marks the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Searches for a word in the trie."""
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Checks if there is any word in the trie that starts with the given prefix."""
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

# Example Usage
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("apricot")

    print(f"Search 'apple': {trie.search('apple')}")  # True
    print(f"Search 'app': {trie.search('app')}")      # True
    print(f"Search 'banana': {trie.search('banana')}") # False

    print(f"Starts with 'ap': {trie.starts_with('ap')}") # True
    print(f"Starts with 'ban': {trie.starts_with('ban')}") # False
    print(f"Starts with 'applepie': {trie.starts_with('applepie')}") # False (only 'apple' exists as a full word)

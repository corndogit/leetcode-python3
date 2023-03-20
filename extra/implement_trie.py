from typing import Set


class TrieNode:
    def __init__(self, value=""):
        self.value: str = value
        self.children: Set[TrieNode] = set()
        self.is_leaf: bool = False

    def get_child(self, value: str):
        """Returns child of this node with given value if it exists, else return None"""
        for node in self.children:
            if node.value == value:
                return node
        return None

    def create_child(self, child_value: str):
        """Create child at this node with the given value; if a child with this value exists, it is returned"""
        existing_child = self.get_child(child_value)
        if existing_child:
            return existing_child

        new_child = TrieNode(child_value)
        self.children.add(new_child)
        return new_child


class Trie:
    def __init__(self, words: str):
        """
        Instantiate a new trie (AKA prefix tree), a tree-like data structure where the root node is the first
        letter/word of the input string (or list of strings) and every child is the next corresponding
        letter of the string/sentence.
        :param words: a string of characters to construct a trie with
        """
        self.chars = ''
        self.root = TrieNode()

        # create prefix tree from input words
        current_node = self.root
        for char in words:
            current_node = current_node.create_child(char)
        current_node.is_leaf = True

    def search(self, word: str) -> bool:
        """Searches for a complete match of the word in the structure of the trie. Returns true if a path from root
        to leaf is found."""
        curr_node = self.root
        for char in word:
            curr_node = curr_node.get_child(char)
            if not curr_node:
                return False
            if curr_node.is_leaf:
                return True


if __name__ == '__main__':
    strings = ["beans", "bees", "chips"]
    my_trie = Trie(strings[0])
    print(f"Trie({strings[0]}):")
    for s in strings:
        print(f"{s} in trie? {my_trie.search(s)}")

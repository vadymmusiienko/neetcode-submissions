class PrefixTree:

    class Node:
        def __init__(self):
            self.children = [None] * 26 # ord(Letter): Node
            self.end = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if not node.children[idx]:
                node.children[idx] = self.Node()
            
            node = node.children[idx]
        
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if not node.children[idx]:
                return False

            node = node.children[idx]

        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            idx = ord(char) - ord('a')

            if not node.children[idx]:
                return False
            
            node = node.children[idx]
        
        return True
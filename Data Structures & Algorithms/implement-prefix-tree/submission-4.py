class PrefixTree:

    class Node:
        def __init__(self, char="", end=False):
            self.char = char
            self.children = {} # Letter: Node
            self.end = end

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        node = self.root

        for i, char in enumerate(word):
            end = (i == len(word) - 1)

            if char not in node.children:
                node.children[char] = self.Node(char)

            node = node.children[char]

            if end:
                node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        n = len(word)

        for i in range(n):
            char = word[i]
            end = (i == (n - 1))

            if char not in node.children:
                return False
            
            if end:
                return node.children[char].end
            
            node = node.children[char]
        
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]
        
        return True
        
        
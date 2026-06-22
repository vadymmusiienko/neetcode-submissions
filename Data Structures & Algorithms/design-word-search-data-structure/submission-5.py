class WordDictionary:

    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.end = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if not node.children[idx]:
                node.children[idx] = self.TrieNode()
            
            node = node.children[idx]
        
        node.end = True

    def search(self, word: str) -> bool:
        n = len(word)

        def searchHelper(start, node):
            # Empty string base case (i.e. Last char is '.')
            if start >= n:
                return node.end
            
            for idx in range(start, n):
                char = word[idx]

                # Wild card case
                if char == '.':

                    # Try all 26 letters
                    for child in node.children:
                        if not child:
                            continue

                        if searchHelper(idx + 1, child):
                            return True
                    
                    return False
                
                # Normal letter case
                i = ord(char) - ord('a')
                if not node.children[i]:
                    return False
                
                node = node.children[i]
            
            return node.end

        return searchHelper(0, self.root)
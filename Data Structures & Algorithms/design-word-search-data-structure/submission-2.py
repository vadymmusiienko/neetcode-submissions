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

        def searchHelper(word, root):
            #TODO: try passing idx instead of new_word
            # Empty string base case (i.e. Last char is '.')
            if not word:
                return root.end
            
            # TODO: change node to root
            node = root
            
            for idx, char in enumerate(word):

                # Wild card case
                if char == '.':
                    new_word = word[idx + 1::]

                    # Try all 26 letters
                    result = False
                    for child in node.children:
                        if not child:
                            continue

                        result = result or searchHelper(new_word, child)
                    
                    return result
                    # No children (all None)
                    return False
                
                # Normal letter case
                idx = ord(char) - ord('a')
                if not node.children[idx]:
                    return False
                
                node = node.children[idx]
            
            return node.end

        return searchHelper(word, self.root)
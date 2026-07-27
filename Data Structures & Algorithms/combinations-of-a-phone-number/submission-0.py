class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": ["a", "b", "c"], "3": ["d", "e", "f"],
                   "4": ["g", "h", "i"], "5": ["j", "k", "l"], 
                   "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], 
                   "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        res = []
        currWord = []
        def backtrack(idx):
            # Base case: End of the word
            if idx >= len(digits):
                res.append("".join(currWord))
                return
            
            # Try all possible letters
            digit = digits[idx]
            for char in mapping[digit]:
                currWord.append(char)
                backtrack(idx + 1)
                currWord.pop()

        if not digits:
            return []
            
        backtrack(0)
        return res
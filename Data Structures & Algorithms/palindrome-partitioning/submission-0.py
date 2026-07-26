import math
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def isPalindrome(start, end):
            length = (end - start + 1) // 2
            for i in range(length):
                if s[start + i] != s[end - i]:
                    return False
            
            return True

        def backtrack(curSplit, start):
            # Done
            if start == n:
                res.append(curSplit[::]) # Copy
                return

            # Recurse on palindromes only
            for end in range(start, n):

                if isPalindrome(start, end):
                    curSplit.append(s[start:end + 1])
                    backtrack(curSplit, end + 1)
                    curSplit.pop()

        backtrack([], 0)
        return res
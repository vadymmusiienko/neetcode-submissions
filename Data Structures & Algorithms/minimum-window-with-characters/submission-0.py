from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tLen = len(t)
        sLen = len(s)
        if sLen < tLen:
            return ""

        minLen = float("inf")
        pointers = None

        left = 0
        freqs = Counter(t)
        missing = tLen
        for right in range(sLen):

            # Expand the window
            rightChar = s[right]
            if rightChar in freqs:
                freqs[rightChar] -= 1

                if freqs[rightChar] >= 0:
                    missing -= 1

            # Shrink the window
            while not missing:

                # Potential answer
                if minLen > (right - left + 1):
                    minLen = right - left + 1
                    pointers = (left, right) # Used to recreate str
                
                # Shrink the window
                leftChar = s[left]
                if leftChar in freqs:
                    freqs[leftChar] += 1
                    
                    if freqs[leftChar] > 0:
                        missing += 1

                left += 1

        res = "" if not pointers else s[pointers[0]:pointers[1] + 1]

        return res
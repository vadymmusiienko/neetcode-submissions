class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            offset = columnNumber % 26
            letter = chr(offset + ord('A'))
            res.append(letter)
            columnNumber //= 26
        
        res.reverse()
        return "".join(res)
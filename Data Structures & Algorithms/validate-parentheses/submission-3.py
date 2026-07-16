class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', '}':'{', ']':'['} 
        stack = []

        for bracket in s:

            if bracket in pairs:

                if not stack or pairs[bracket] != stack.pop():
                    return False

            else:
                stack.append(bracket)
        
        return not stack


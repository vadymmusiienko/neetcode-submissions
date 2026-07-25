class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def backtrack(openP, closedP):
            # Valid solution
            if openP == closedP == n:
                res.append("".join(cur))
                return

            # Open
            if openP < n:
                cur.append("(")
                backtrack(openP + 1, closedP)
                cur.pop()
            
            # Close
            if openP > closedP:
                cur.append(")")
                backtrack(openP, closedP + 1)
                cur.pop()
            
        
        backtrack(0, 0)
        return res


            

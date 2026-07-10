class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        memo = {n: True}
        def dfs(start):
            if start in memo:
                return memo[start]
            
            for end in range(start, n):

                if s[start:end + 1] in wordDict:
                    memo[start] = dfs(end+1)

                    if memo[start]:
                        return True

            memo[start] = False
            return memo[start]
        
        return dfs(0)
        
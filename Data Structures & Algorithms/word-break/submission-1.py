class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        memo = {n: True}
        def dfs(start):
            if start in memo:
                return memo[start]
            
            end = start
            while end < n:

                if s[start:end + 1] in wordDict:
                    memo[start] = dfs(end+1)

                    if memo[start]:
                        return True

                end += 1
            
            memo[start] = False
            return memo[start]
        
        return dfs(0)
        
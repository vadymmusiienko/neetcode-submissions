class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}
        def dfs(i, j, curL):
            if i < 0 or j < 0:
                return curL
            
            triplet = (i, j, curL)
            if triplet in memo:
                return memo[triplet]
            
            # Match
            if text1[i] == text2[j]:
                memo[triplet] = dfs(i - 1, j - 1, curL + 1)
            else:
                memo[triplet] = max(dfs(i - 1, j, curL), dfs(i, j -1, curL))
        
            return memo[triplet]

        return dfs(len(text1) - 1, len(text2) - 1, 0)
            

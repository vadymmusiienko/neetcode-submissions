class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp1 = 1 # i + 1
        dp2 = 0 # i + 2
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                new_dp = 0
            else:
                new_dp = dp1
                
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
                new_dp += dp2
            
            dp2 = dp1
            dp1 = new_dp

        return dp1


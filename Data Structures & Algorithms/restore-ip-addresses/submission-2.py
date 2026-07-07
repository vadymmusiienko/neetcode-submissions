class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12:
            return []
        res = []
        def backtrack(idx, parts):
            if idx == n and len(parts) == 4:
                res.append(".".join(parts))
                return
            
            if len(parts) > 4 or idx >= n:
                return
            
            if s[idx] == "0":
                backtrack(idx + 1, parts + ["0"])
                return

            # 0, 1, 2
            for i in range(min(3, n - idx)):
                if int(s[idx:idx+i+1]) < 256:
                    backtrack(idx + i + 1, parts + [s[idx:idx+i+1]])
        
        backtrack(0, [])
        return res
                

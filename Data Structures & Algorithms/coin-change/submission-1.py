class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0 : 0}
        def dfs(target):
            if target in memo:
                return memo[target]
            if target < 0:
                return -1

            if target == 0:
                return 0

            res = -1
            for coin in coins:
                tmp = dfs(target - coin)
                if tmp == -1:
                    continue

                tmp += 1
                if res == -1:
                    res = tmp
                else:
                    res = min(res, tmp)
            
            memo[target] = res
            return res

        return dfs(amount)
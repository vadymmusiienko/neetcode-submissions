class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n):
            temp = temperatures[i]

            while stack and stack[-1][0] < temp:
                _, idx = stack.pop()
                res[idx] = i - idx
            
            stack.append((temp, i))

        return res
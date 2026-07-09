class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n in seen:
                return False

            if n == 1:
                return True

            seen.add(n)
            new_n = 0
            for d in str(n):
                new_n += int(d) ** 2
            
            n = new_n
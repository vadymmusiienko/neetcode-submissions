class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        # s2 is shorter - hence can't have s1 in it
        if len(s2) < n:
            return False
        
        s1_freqs = [0] * 26
        s2_freqs = [0] * 26

        # Create s1 freq map
        for char in s1:
            idx = ord(char) - ord('a')
            s1_freqs[idx] += 1
        
        left = 0
        for right in range(len(s2)):
            r_idx = ord(s2[right]) - ord('a')
            s2_freqs[r_idx] += 1

            if right - left + 1 >= n:

                if s2_freqs == s1_freqs:
                    return True

                l_idx = ord(s2[left]) - ord('a')
                s2_freqs[l_idx] -= 1
                left += 1
        
        return False


        

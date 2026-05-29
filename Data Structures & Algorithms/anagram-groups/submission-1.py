class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def get_freq_map(s):
            freq_map = [0] * 26

            for char in s:
                freq_map[ord(char) - ord("a")] += 1 
            
            return tuple(freq_map)
        
        anagram_clusters = {}
        for word in strs:

            freq_map = get_freq_map(word)

            if freq_map in anagram_clusters:
                anagram_clusters[freq_map].append(word)
            else:
                anagram_clusters[freq_map] = [word]
            
        return list(anagram_clusters.values())



        

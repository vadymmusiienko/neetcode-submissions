class Solution:

    # User '<length of next word> + #' 
    def encode(self, strs: List[str]) -> str:
        encoded_str_list = []
        
        for s in strs:
            encoded_str_list.append(f"{len(s)}#")
            encoded_str_list.append(s)
        
        print("".join(encoded_str_list))
        return "".join(encoded_str_list)

    def decode(self, s: str) -> List[str]:
        decoded_str_list = []

        i = 0
        while i < len(s):

            # Find the word length
            word_len_list = []
            while s[i].isdigit():
                word_len_list.append(s[i])
                i += 1

            word_len = int("".join(word_len_list))
            
            # Skip "#"
            decoded_str_list.append(s[i + 1:i+word_len + 1])
            i += word_len + 1

        return decoded_str_list

            

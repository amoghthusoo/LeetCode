class Solution:
    def repeatedCharacter(self, s: str) -> str:

        char_dict = {}

        for ch in s:
            
            if(ch not in char_dict):
                char_dict[ch] = None
            else:
                return ch

                
            
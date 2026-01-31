class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        small_dict = {}
        capital_dict = {}

        for ch in word:

            if(ch.islower() and ch not in small_dict):
                small_dict[ch] = None
            
            elif(ch not in capital_dict):
                capital_dict[ch] = None


        count = 0
        for key, val in small_dict.items():
            if(key.upper() in capital_dict):
                count += 1

        return count

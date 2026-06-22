class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        target_letters = {"b", "a", "l", "o", "n"}

        freq_dict = dict()
        for ch in text:
            if(ch in target_letters):
                freq_dict[ch] = freq_dict.get(ch, 0) + 1
        
        if(len(freq_dict) != 5):
            return 0

        freq_dict["l"] //= 2
        freq_dict["o"] //= 2

        return int(min(freq_dict.values()))               
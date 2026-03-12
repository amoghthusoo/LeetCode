class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        
        ans = ""
        for word in words:
            temp = 0
            for ch in word:
                temp += weights[ord(ch) - 97]
            temp %= 26
            
            ans += chr(122 - temp)
        
        return ans
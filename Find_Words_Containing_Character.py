class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        
        out_arr = []

        for i, word in enumerate(words):
            if(x in word):
                out_arr.append(i)

        return out_arr
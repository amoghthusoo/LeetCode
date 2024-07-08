class Solution:
    def numDifferentIntegers(self, word: str) -> int:
    
        i = 0
        while (i < len(word)):
            if (not word[i].isdigit()):
                word = word.replace(word[i], " ")

            i += 1

        word = word.split()
        word = [int(e) for e in word]
        word = list(set(word))
        return len(word)

from collections import Counter
class Solution:
    def uniqueMorseRepresentations(self, words: list) -> int:
        
        alphabets = [chr(i) for i in range(97, 123)]
        morseRep = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        encryptDict = dict(zip(alphabets, morseRep))
        interList = ["" for i in range(len(words))]

        i = 0
        while (i < len(words)):
            
            j = 0
            while (j < len(words[i])):

                interList[i] += encryptDict[words[i][j]]

                j += 1

            i += 1

        occDict = dict(Counter(interList))

        print(interList)

        return len(list(occDict.keys()))

words = ["gin","zen","gig","msg"]
obj = Solution()
solution = obj.uniqueMorseRepresentations(words)
print(solution)
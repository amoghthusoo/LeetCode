class Solution:

    def removeCharacter(self, string, index) -> str:
        
        outStr = ""

        i = 0
        while(i < len(string)):

            if(i != index):
                outStr += string[i]

            i += 1

        return outStr

    def commonChars(self, words: list[str]) -> list[str]:
        
        outArr = []

        for character in words[0]:
            
            for word in words:
                if(character not in word):
                    break
                
                characterIndex = word.index(character)
                words[words.index(word)] = self.removeCharacter(word, characterIndex)
            
            else:
                outArr.append(character)

        return outArr

words = ["bella","label","roller"]
obj = Solution()
out = obj.commonChars(words)
print(out)
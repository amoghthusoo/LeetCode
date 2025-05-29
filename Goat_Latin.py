class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        sentence = sentence.split()

        out = ""
        for i, word in enumerate(sentence):

            if(word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]):
                out += word + "ma"
            else:
                out += word[1:] + word[0] + "ma"
            
            for _ in range(i + 1):
                out += "a"

            if(i != len(sentence) - 1):
                out += " "

        return out
    
sentence = "I speak Goat Latin"
obj = Solution()
out = obj.toGoatLatin(sentence)
print(out)

from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        
        lp_occr_dict = Counter(licensePlate.lower())
        intr_arr = []
        
        for i, word in enumerate(words):
            word_occr_dict = Counter(word)

            for letter, freq in lp_occr_dict.items():

                if(letter.isalpha()):

                    if(freq <= word_occr_dict[letter]):
                        pass
                    else:
                        break
            
            else:
                intr_arr.append((len(word), i))


        intr_arr.sort()
        return words[intr_arr[0][1]]
    

licensePlate = "1s3 456"
words = ["looks","pest","stew","show"]
obj = Solution()
result = obj.shortestCompletingWord(licensePlate, words)
print(result)

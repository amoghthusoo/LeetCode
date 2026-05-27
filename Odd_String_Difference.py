from collections import Counter
class Solution:
    def oddString(self, words: list[str]) -> str:
        
        intr_dict = dict()

        for word in words:
            diff = []
            for i in range(len(word) - 1):
                diff.append(ord(word[i + 1]) - ord(word[i]))
                
            diff = tuple(diff)
            if(diff not in intr_dict):
                intr_dict[diff] = [word]
            else:
                intr_dict[diff].append(word)

        for diff, w in intr_dict.items():

            if(len(w) == 1):
                return next(iter(w))

words = ["adc","wzy","abc"]
obj = Solution()
result = obj.oddString(words)
print(result)

    
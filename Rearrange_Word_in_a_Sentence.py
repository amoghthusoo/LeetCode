class Solution:
    def arrangeWords(self, text: str) -> str:
        
        words = text.split()
        intr_arr = []

        for i, word in enumerate(words):
            intr_arr.append((len(word), i))
        
        intr_arr.sort()

        first_word = True
        ans = ""
        for i, e in enumerate(intr_arr):

            if(first_word):
                ans += words[e[1]].capitalize()
                first_word = False

                if(i != len(intr_arr) - 1):
                    ans += " "
                
                continue

            if(e[1] == 0):
                ans += words[e[1]].lower()
            else:
                ans += words[e[1]]

            if(i != len(intr_arr) - 1):
                ans += " "
        
        return ans 

text = "Leetcode is cool"
obj = Solution()
result = obj.arrangeWords(text)
print(result)
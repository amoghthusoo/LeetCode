class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:

        text = text.split()

        ans = []
        i = 0
        while(i < len(text) - 2):

            if(text[i] == first and text[i + 1] == second):
                ans.append(text[i + 2])

            i += 1
        
        return ans

text = "alice is a good girl she is a good student"
first = "a"
second = "good"
obj = Solution()
result = obj.findOcurrences(text, first, second)
print(result)
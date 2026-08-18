class Solution:
    def generateTag(self, caption: str) -> str:

        caption = caption.split()
        ans = "#"

        if(len(caption) == 0):
            return ans

        ans += caption[0].lower()

        for i in range(1, len(caption)):
            ans += caption[i].capitalize()

        if(len(ans) <= 100):
            return ans
        else:
            return ans[0:100]
        

caption = "Leetcode daily streak achieved"
obj = Solution()
result = obj.generateTag(caption)
print(result)
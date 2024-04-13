class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        title = title.split()
        outStr = ""

        x = 0
        for word in title:
            if(len(word) in [1, 2]):
                outStr += word.lower()
            else:
                outStr += word.capitalize()
                pass
            
            if(x != len(title) - 1):
                outStr += " "

            x += 1

            
        return outStr

title = "capiTalIze tHe titLe"
obj = Solution()
out = obj.capitalizeTitle(title)
print(out)
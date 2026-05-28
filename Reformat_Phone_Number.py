class Solution:
    def reformatNumber(self, number: str) -> str:
        
        number = number.replace(" ", "")
        number = number.replace("-", "")

        if(len(number) < 3):
            return number

        ans = ""

        i = 0
        while(len(number) - i > 4):

            ans += number[i : i + 3] + "-"
            i += 3
        
        if(len(number) - i == 4):
            ans += number[i : i + 2] + "-" + number[i + 2 : ] 
        elif(len(number) - i == 3):
            ans += number[i : ]
        else:
            ans += number[i : ]

        return ans
    
number = "9964-"
obj = Solution()
result = obj.reformatNumber(number)
print(result)
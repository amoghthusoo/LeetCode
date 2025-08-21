class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        temp = num1.split("+")
        a = int(temp[0])
        b = int(temp[1].replace("i", ""))

        temp = num2.split("+")
        c = int(temp[0])
        d = int(temp[1].replace("i", ""))

        real = a * c - b * d
        img = a * d + b * c

        return f"{real}+{img}i"
    
num1 = "1+-1i"
num2 = "1+-1i"

obj = Solution()
result = obj.complexNumberMultiply(num1, num2)
print(result)
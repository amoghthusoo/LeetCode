class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        indices = []

        for i, e in enumerate(number):
            if(e == digit):
                indices.append(i)

        max_num = -1
        
        for i in indices:

            temp = int(number[0:i] + number[i + 1 :])   
            if(temp > max_num):
                max_num = temp

        return str(max_num)
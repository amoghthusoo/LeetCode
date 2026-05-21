class Solution:
    def concatHex36(self, n: int) -> str:
        
        p = n * n
        hexa_decimal = hex(p)[2 : ]

        temp = ""
        for i, e in enumerate(hexa_decimal):
            if(e.isalpha()):
                temp += e.capitalize()
            else:
                temp += e
        hexa_decimal = temp

        q = n * n * n

        hexa_trigesimal = ""

        while(q != 0):

            r = q % 36
            if(r <= 9):
                hexa_trigesimal += str(r)
            else:
                hexa_trigesimal += chr(r + 55)
            q //= 36
        
        hexa_trigesimal = hexa_trigesimal[-1 : :-1]

        return hexa_decimal + hexa_trigesimal

n = 13
obj = Solution()
result = obj.concatHex36(n)
print(result)
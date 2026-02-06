class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        
        if(k == 0):
            return [0 for _ in range(len(code))]

        ans = []

        i = 0
        while(i < len(code)):
            
            total = 0

            if(k > 0):
                j = (i + 1) % len(code)
            elif(k < 0):
                j = (i - 1) % len(code)

            for _ in range(abs(k)):
                total += code[j % len(code)]

                if(k > 0):
                    j += 1
                elif(k < 0):
                    j -= 1
            
            ans.append(total)
            
            i += 1

        return ans

code = [2,4,9,3]
k =  -2
obj = Solution()
result = obj.decrypt(code, k)
print(result)

class Solution:
    
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        
        num_string = ""
        for digit in num:
            num_string += str(digit)
        
        inter_string = str(int(num_string) + k)

        out_arr = []

        for digit in inter_string:
            out_arr.append(int(digit))

        return out_arr
        

num = [1,2,0,0]
k = 34
obj = Solution()
out = obj.addToArrayForm(num, k)
print(out)

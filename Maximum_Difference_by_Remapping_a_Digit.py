class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        first_non_nine_digit = None
        for e in str(num):
            if(e != "9"):
                first_non_nine_digit = e
                break

        if(first_non_nine_digit == None):
            first_non_nine_digit = "9"
        
        first_non_zero_digit = None
        for e in str(num):
            if(e != "0"):
                first_non_zero_digit = e
                break
        
        max_num = str(num).replace(first_non_nine_digit, "9")
        min_num = str(num).replace(first_non_zero_digit, "0")

        return int(max_num) - int(min_num)

num = 99999
obj = Solution()
result = obj.minMaxDifference(num)
print(result)
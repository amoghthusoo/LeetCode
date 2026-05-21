class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        
        prefixes = set()

        for num in arr1:
            num = str(num)

            temp = ""
            for digit in num:
                temp += digit
                prefixes.add(temp)
        

        ans = 0
        for num in arr2:
            num = str(num)

            temp = ""
            for digit in num:
                temp += digit

                if(temp in prefixes):
                    ans = max(ans, len(temp))
    
        return ans 

arr1 = [1,10,100]
arr2 = [1000]
obj = Solution()
result = obj.longestCommonPrefix(arr1, arr2)
print(result)
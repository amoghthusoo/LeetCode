class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        num_str = str(num)
        ans = 0
        i = 0
        while(i < len(num_str) - k + 1):

            sub_str = num_str[i : i + k]

            try:
                if(num % int(sub_str) == 0):
                    ans += 1
            except:
                pass

            i += 1

        return ans
    
num = 430043
k = 2
obj = Solution()
result = obj.divisorSubstrings(num, k)
print(result)

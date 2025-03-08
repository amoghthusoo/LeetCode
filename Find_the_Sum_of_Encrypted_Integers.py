class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        
        out = 0

        for num in nums:

            max_digit = max([int(x) for x in str(num)])

            temp_str = ""
            for _ in range(len(str(num))):
                temp_str += str(max_digit)

            out += int(temp_str)

        return out

            
nums = [1,2,3]
obj = Solution()
out = obj.sumOfEncryptedInt(nums)
print(out)

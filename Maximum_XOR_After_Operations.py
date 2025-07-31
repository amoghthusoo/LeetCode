class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        
        bin_arr = [0 for _ in range(27)]

        for num in nums:
            bin_str = bin(num)[2 : ]
            i = len(bin_str) - 1
            j = len(bin_arr) - 1
            while(i >= 0):
                
                if(bin_str[i] == "1"):

                    if(bin_arr[j] % 2 == 0):
                        bin_arr[j] += 1
                
                i -= 1
                j -= 1

        result_bin_str = ""
        for e in bin_arr:
            result_bin_str += str(e)

        return int(result_bin_str, 2)


nums = [3,2,4,6]
solution = Solution()
result = solution.maximumXOR(nums)
print(result)
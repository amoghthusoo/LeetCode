class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        num_set = set()

        for num in nums:
            num_set.add(int(num, 2))

        i = 0
        while(True):
            
            if(i not in num_set):
                return bin(i)[2 : ].zfill(len(nums))
            
            i += 1

nums = ["111","011","001"]
solution = Solution()
result = solution.findDifferentBinaryString(nums)
print(result)
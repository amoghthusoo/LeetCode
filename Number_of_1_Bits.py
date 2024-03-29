class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # binNum = bin(n)[2:]
        # count = binNum.count("1")
        # print(count)

        return bin(n)[2:].count("1")

n = 11
obj = Solution()
out = obj.hammingWeight(n)
print(out)
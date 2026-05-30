class Solution:
    def reverseBits(self, n: int) -> int:
        
        return int(bin(n)[2 : ].zfill(32)[-1 : : -1], 2)
        


n = 43261596
obj = Solution()
result = obj.reverseBits(n)
print(result)
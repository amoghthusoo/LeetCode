class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        
        total = 0
        for i in range(1, len(arr) + 1, 2):

            for j in range(len(arr) + 1 - i):

                total += sum(arr[j : j + i])

        return total
                
        

arr = [10,11,12]
obj = Solution()
solution = obj.sumOddLengthSubarrays(arr)
print(solution)
from collections import Counter
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        
        freq = sorted(Counter(arr).values(), reverse = True)

        total = 0
        i = 0
        while(i < len(freq)):
            total += freq[i]
            i += 1

            if(total >= len(arr) // 2):
                return i


arr = [3,3,3,3,5,5,5,2,2,7]
obj = Solution()
result = obj.minSetSize(arr)
print(result)
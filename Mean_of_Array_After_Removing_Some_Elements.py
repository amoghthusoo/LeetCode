from statistics import mean
class Solution:
    def trimMean(self, arr: list) -> float:
        
        arr.sort()
        n = int(0.05 * len(arr))     # No. of elements to be trimmed.

        for i in range(n):
            del(arr[0])
            del(arr[-1])

        _mean = round(mean(arr), 5)

        return _mean

arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
obj = Solution()
solution = obj.trimMean(arr)
print(solution)
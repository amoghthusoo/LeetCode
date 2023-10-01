class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        
        count = 0

        i = 0
        while (i < len(arr)):

            j = i + 1
            while (j < len(arr)):

                k = j + 1
                while (k < len(arr)):

                    if ((abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c)):
                        count += 1


                    k += 1

                j += 1

            i += 1

        return count

arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
obj = Solution()
solution = obj.countGoodTriplets(arr, a, b, c)
print(solution)
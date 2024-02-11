class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        
        i = 0
        while (i < len(arr) - 1):

            j = 0
            while (j < len(arr) - 1):

                if (bin(arr[j]).count('1') > bin(arr[j + 1]).count('1')):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                elif (bin(arr[j]).count('1') == bin(arr[j + 1]).count('1')):

                    if (arr[j] > arr[j + 1]):
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

                j += 1
            i += 1

        return arr


arr = [1024,512,256,128,64,32,16,8,4,2,1]
obj = Solution()
solution = obj.sortByBits(arr)
print(solution)
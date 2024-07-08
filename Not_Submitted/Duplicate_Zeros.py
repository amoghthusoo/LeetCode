class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """     

        i = 0
        while(i < len(arr)):
            
            if(arr[i] == 0):
                arr.insert(i + 1, 0)
                arr.pop()

                i += 2
                continue

            i += 1

arr = [1,2,3]
obj = Solution()
obj.duplicateZeros(arr)
print(arr)
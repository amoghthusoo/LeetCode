class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        
        if(len(arr) < 3):
            return False
        
        max_element = max(arr)
        max_index = arr.index(max_element)

        if(max_index in [len(arr) - 1, 0]):
            return False

        i = 0
        while(i < max_index):
            if(arr[i] >= arr[i + 1]):
                return False
        
            i += 1

        i = max_index
        while(i < len(arr) - 1):

            if(arr[i] <= arr[i + 1]):
                return False

            i += 1

        return True
    
arr = [3,5,5]
obj = Solution()
out = obj.validMountainArray(arr)
print(out)
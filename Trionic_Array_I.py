class Solution:

    def is_increasing(self, arr, l, u):

        i = l
        while(i <= u - 1):

            if(arr[i] >= arr[i + 1]):
                return False

            i += 1

        return True

    def is_decreasing(self, arr, l, u):

        i = l
        while(i <= u - 1):

            if(arr[i] <= arr[i + 1]):
                return False

            i += 1

        return True


    def isTrionic(self, nums: list[int]) -> bool:
        

        i = 1
        while(i < len(nums) - 2):
            j = i + 1
            while(j < len(nums) - 1):

                if(self.is_increasing(nums, 0, i) and self.is_decreasing(nums, i, j) and self.is_increasing(nums, j, len(nums) - 1)):
                    return True

                j += 1
            i += 1

        return False
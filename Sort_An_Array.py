class Solution:

    def merge(self, left_array, right_array, array):

        left_size = len(array) // 2
        right_size = len(array) - left_size

        i = 0
        l = 0
        r = 0

        while(l < left_size and r < right_size):

            if(left_array[l] < right_array[r]):
                array[i] = left_array[l]
                i += 1
                l += 1

            else:

                array[i] = right_array[r]
                i += 1
                r += 1

        while(l < left_size):

            array[i] = left_array[l]
            i += 1
            l += 1

        while(r < right_size):

            array[i] = right_array[r]
            i += 1
            r += 1

    def merge_sort(self, array):

        length = len(array)
        if(length <= 1):
            return
        
        middle = length // 2

        left_array = [0 for i in range(middle)]
        right_array = [0 for i in range(length - middle)]

        i = 0
        j = 0

        while(i < length):

            if(i < middle):
                left_array[i] = array[i]
                i += 1
            else:
                right_array[j] = array[i]
                i += 1
                j += 1

        self.merge_sort(left_array)
        self.merge_sort(right_array)
        self.merge(left_array, right_array, array)

    def sortArray(self, nums: list[int]) -> list[int]:
        self.merge_sort(nums)
        return nums
class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        
        def left_shift(arr, k):

            part1 = arr[:k]
            part2 = arr[k:]
            return part2 + part1

        def right_shift(arr, k):

            k = len(arr) - k
            part1 = arr[:k]
            part2 = arr[k:]
            return part2 + part1

        k %= len(mat[0])
        for i, row in enumerate(mat):

            if(i % 2 == 0):
                if(row != left_shift(row, k)):
                    return False
            else:
                if(row != right_shift(row, k)):
                    return False
        
        return True
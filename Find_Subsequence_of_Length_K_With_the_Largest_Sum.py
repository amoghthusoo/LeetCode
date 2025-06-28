class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        
        indexed_arr = []
        for i, e in enumerate(nums):
            indexed_arr.append([e, i])

        indexed_arr.sort()


        required_elements = indexed_arr[-1 : -1 - k : -1]
        required_elements.sort(key = lambda x : x[1])

        ans = [required_elements[i][0] for i in range(len(required_elements))]

        return ans
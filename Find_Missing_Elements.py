class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:

        num_set = set()
        _min = nums[0]
        _max = nums[0]

        for e in nums:

            if(e < _min):
                _min = e
            
            if(e > _max):
                _max = e

            num_set.add(e)

        ans = []
        for i in range(_min + 1, _max):
            if(i not in num_set):
                ans.append(i)

        return ans
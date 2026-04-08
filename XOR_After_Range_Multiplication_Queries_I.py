class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = int(10 ** 9) + 7

        for query in queries:
            li = query[0]
            ri = query[1]
            ki = query[2]
            vi = query[3]

            idx = li
            while(idx <= ri):
                nums[idx] = (nums[idx] * vi) % MOD
                idx += ki
        
        res = 0
        for num in nums:
            res ^= num
        
        return res


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        not_seen = set()
        for i in range(1, k + 1):
            not_seen.add(i)

        ans = 0
        i = len(nums) - 1
        while(not_seen):
            not_seen.discard(nums[i])
            ans += 1
            i -= 1

        return ans
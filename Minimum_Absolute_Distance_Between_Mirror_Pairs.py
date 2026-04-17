class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        
        def reverse(num):
            return int(str(num)[::-1].lstrip("0"))
  
        visited = dict()

        ans = float("inf")
        for i, num in enumerate(nums):

            if(num in visited):
                ans = min(ans, abs(i - visited[num]))
            
            else:
                visited[reverse(num)] = i

        return ans if ans != float("inf") else -1

nums = [21, 120]
obj = Solution()
result = obj.minMirrorPairDistance(nums)
print(result)
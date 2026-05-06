class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        
        nums.sort()

        out = []

        for query in queries:
            total = 0
            for i, num in enumerate(nums):
                total += num
                
                if(total > query):
                    out.append(i)
                    break
            else:
                out.append(len(nums))

        return out

nums = [2,3,4,5]
queries = [1]
obj = Solution()
out = obj.answerQueries(nums, queries)
print(out)
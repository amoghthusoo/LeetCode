class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        
        map = dict()
        occr = 0
        for i, e in enumerate(nums):
            
            if(e == x):
                occr += 1
                map[occr] = i

        ans = []
        for query in queries:
            if(query not in map):
                ans.append(-1)
            else:
                ans.append(map[query])
        
        return ans

nums = [1,3,1,7]
queries = [1,3,2,4]
x = 1
obj = Solution()
result = obj.occurrencesOfElement(nums, queries, x)
print(result)

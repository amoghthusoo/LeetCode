class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        
        components = []
        temp = [0]

        i = 1
        while(i < len(nums)):

            if(nums[i] - nums[i - 1] <= maxDiff):
                temp.append(i)
            
            else:
                components.append(temp.copy())
                temp.clear()
                temp.append(i)

            i += 1
        
        components.append(temp)
        
        comp_map = dict()
        for  comp in components:

            start = comp[0]
            end = comp[-1]

            for i in range(start, end + 1):
                comp_map[i] = [start, end]
        
        ans = []
        for query in queries:

            src = query[0]
            dest = query[1]

            component = comp_map[src]

            if(dest >= component[0] and dest <= component[1]):
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
        


n = 4
nums = [2,5,6,8]
maxDiff = 2
queries = [[0,1],[0,2],[1,3],[2,3]]
obj = Solution()
result = obj.pathExistenceQueries(n, nums, maxDiff, queries)
print(result)
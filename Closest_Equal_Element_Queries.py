class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        
        idx_dict = dict()

        for i, num in enumerate(nums):
            if(num not in idx_dict):
                idx_dict[num] = [i]
            else:
                idx_dict[num].append(i)

        idx_idx_dict = dict()

        for key, value in idx_dict.items():
            temp_dict = dict()

            for i, e in enumerate(value):
                temp_dict[e] = i
            
            idx_idx_dict[key] = temp_dict
        
        ans = []

        for query in queries:

            target = nums[query]

            if(len(idx_dict[target]) == 1):
                ans.append(-1)
            
            else:

                i = idx_idx_dict[target][query]
                l = idx_dict[target][(i - 1) % len(idx_dict[target])]
                r = idx_dict[target][(i + 1) % len(idx_dict[target])]
                m = query

                min_dist = min(abs(m - l), len(nums) - abs(m - l), abs(r - m), len(nums) - abs(r - m))
                
                ans.append(min_dist)
        
        return ans
    


nums = [1,3,1,4,1,3,2]
queries = [0,3,5]
obj = Solution()
result = obj.solveQueries(nums, queries)
print(result)

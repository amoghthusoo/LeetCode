from sortedcontainers import SortedList
class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        
        index_dict = {}

        for i, e in enumerate(nums):
            if(e not in index_dict):
                index_dict[e] = SortedList([i])
            else:
                index_dict[e].add(i)
        
        ans = 2 ** 31 - 1
        for indices in index_dict.values():
            if(len(indices) >= 3):
                
                i = 0
                while(i < len(indices) - 2):

                    ans = min(ans, abs(indices[i] - indices[i + 1]) + abs(indices[i + 1] - indices[i + 2]) + abs(indices[i + 2] - indices[i]))

                    i += 1
        
        return ans if ans != 2 ** 31 - 1 else -1
    
nums = [1,2,1,1,3]
obj = Solution()
result = obj.minimumDistance(nums)
print(result)
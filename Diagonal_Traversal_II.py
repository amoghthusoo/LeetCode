class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:

        group_dict = dict()

        for i, row in enumerate(nums):
            for j, element in enumerate(row):
                
                if(i + j not in group_dict):
                    group_dict[i + j] = [element]
                else:
                    group_dict[i + j].append(element)
        
        ans = []

        for _, diagonal in group_dict.items():

            i = -1
            while(i >= -len(diagonal)):
                ans.append(diagonal[i])
                i -= 1
            
        return ans

nums = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
result = obj.findDiagonalOrder(nums)
print(result)

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        
        group_dict = dict()

        for i, row in enumerate(mat):
            for j, element in enumerate(row):
                
                if(i + j not in group_dict):
                    group_dict[i + j] = [element]
                else:
                    group_dict[i + j].append(element)
        
        ans = []

        for key, diagonal in group_dict.items():

            if(key % 2 == 0):

                i = -1
                while(i >= -len(diagonal)):
                    ans.append(diagonal[i])
                    i -= 1

            else:
                i = 0
                while(i < len(diagonal)):
                    ans.append(diagonal[i])
                    i += 1

        return ans


mat = [[1,2],[3,4]]
obj = Solution()
result = obj.findDiagonalOrder(mat)
print(result)

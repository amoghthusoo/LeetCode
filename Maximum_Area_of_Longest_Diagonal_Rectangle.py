class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        
        diagonal_dict = {}

        for dimension in dimensions:
            diagonal_dict[tuple(dimension)] = (dimension[0] ** 2 + dimension[1] ** 2) ** 0.5

        
        max_diagonal = max(diagonal_dict.values())

        possible_rect = []

        for key, value in diagonal_dict.items():

            if(value == max_diagonal):
                possible_rect.append(key)

        area_list = []

        for rect in possible_rect:
            area_list.append(rect[0] * rect[1])

        return max(area_list)
    
dimensions = [[9,3],[8,6]]
obj = Solution()
out = obj.areaOfMaxDiagonal(dimensions)
print(out)
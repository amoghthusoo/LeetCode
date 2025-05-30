class Solution:
    def findChampion(self, grid: list[list[int]]) -> int: 

        occr_dict = {}
    
        for i, row in enumerate(grid):
            occr_dict[i] = row.count(1)

        _max = -1
        for key, val in occr_dict.items():
            if(val > _max):
                _max = val

        for key, val in occr_dict.items():
            if(val == _max):
                return key
            
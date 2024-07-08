class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        
        root_val = int(area ** 0.5)

        while(True):

            if(area % root_val == 0):
                return [int(area / root_val), root_val]
            
            root_val -= 1

area = 122122
obj = Solution()
out = obj.constructRectangle(area)
print(out)
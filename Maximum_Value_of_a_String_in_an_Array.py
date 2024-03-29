class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        
        maxValue = -1

        for string in strs:

            if(string.isdigit()):
                value = int(string)
            else:
                value = len(string)

            if(value > maxValue):
                maxValue = value
        
        return maxValue

strs = ["1","01","001","0001"]
obj = Solution()
out = obj.maximumValue(strs)
print(out)
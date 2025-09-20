class Solution:
    def partitionString(self, s: str) -> int:
        
        count = 0
        temp_set = set()
        for ch in s:
            if(ch in temp_set):
                count += 1
                temp_set.clear()
                temp_set.add(ch)
            else:
                temp_set.add(ch)
        
        
        return count + 1

s = "ssssss"
solution = Solution()
result = solution.partitionString(s)
print(result)
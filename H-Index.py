class Solution:
    def hIndex(self, citations: list[int]) -> int:
        
        citations.sort(reverse = True)
        i = 0
        while(i < len(citations)):

            if(citations[i] < i + 1):
                return i

            i += 1
        
        return i

citations = [3,0,6,1,5]
obj = Solution()
result = obj.hIndex(citations)
print(result)
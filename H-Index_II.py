class Solution:
    def hIndex(self, citations: list[int]) -> int:
        
        i = len(citations) - 1
        while(i >= 0):

            if(citations[i] < len(citations) - i):
                return len(citations) - i - 1

            i -= 1
        
        return len(citations)

citations = [1,2,100]
obj = Solution()
result = obj.hIndex(citations)
print(result)
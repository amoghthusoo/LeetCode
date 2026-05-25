from heapq import *

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        heap = []

        for i, ch in enumerate(s):
            if(ch != "*"):
                heappush(heap, (ch, -i))
            else:
                heappop(heap)
        
        heap.sort(key = lambda e : -e[1])

        ans = ""
        for e in heap:
            ans += e[0]
        
        return ans

s = "aaba*"
obj = Solution()
result = obj.minimizeStringValue(s)
print(result)
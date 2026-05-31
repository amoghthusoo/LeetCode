import heapq

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:

        for i, e in enumerate(gifts):
            gifts[i] = e * (-1)

        heapq.heapify(gifts)

        for _ in range(k):
            popped = heapq.heappop(gifts) * (-1)
            popped = int(popped ** 0.5) * (-1)
            heapq.heappush(gifts, popped)
        
        return sum(gifts) * (-1)
    
gifts = [25,64,9,4,100]
k = 4
obj = Solution()
result = obj.pickGifts(gifts, k)
print(result)
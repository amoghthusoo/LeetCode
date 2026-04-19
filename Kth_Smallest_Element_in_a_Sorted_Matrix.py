import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:

        heap = []

        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        count = 0
        while(count != k):

            popped = heapq.heappop(heap)

            r = popped[1]
            c = popped[2]

            if(c + 1 < len(matrix)):
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

            count += 1

        return popped[0]        
    
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
obj = Solution()
result = obj.kthSmallest(matrix, k)
print(result)
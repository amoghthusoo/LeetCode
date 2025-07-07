import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        
        events.sort(key = lambda x : (x[0], x[1]))

        min_heap = []
        count = 0
        day = events[0][0]
        i = 0
        while(i < len(events) or min_heap):
            
            while(i < len(events) and events[i][0] <= day):
            
                heapq.heappush(min_heap, events[i][1])
                i += 1

            while (min_heap and min_heap[0] < day):
                heapq.heappop(min_heap)

            if(min_heap):
                heapq.heappop(min_heap)
                count += 1
        
            day += 1

        return count
        
    
events = [[52,79],[7,34]]
obj = Solution()
result = obj.maxEvents(events)
print(result)
class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:

        _start = min(start, destination)
        _dest = max(start, destination)
        
        total_dist = sum(distance)
        
        dist_1 = 0
        i = _start
        while(i < _dest):

            dist_1 += distance[i]
            i += 1

        dist_2 = total_dist - dist_1
        return min(dist_1, dist_2)


distance = [1,2,3,4]
start = 0
destination = 3
obj = Solution()
result = obj.distanceBetweenBusStops(distance, start, destination)
print(result)

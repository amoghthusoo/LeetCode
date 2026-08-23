class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        
        intr_ans = []
        for idx, drone in enumerate(drones):

            dx = drone[0]
            dy = drone[1]
            ran = drone[2]

            tx = target[0]
            ty = target[1]

            dist = abs(tx - dx) + abs(ty - dy)

            if(dist <= ran):
                intr_ans.append((dist, idx))

        if(intr_ans):
            intr_ans.sort()
            return intr_ans[0][1]

        return -1

drones = [[0,0,8],[2,2,9]]
target = [3,4]
obj = Solution()
result = obj.nearestDrone(drones, target)
print(result)
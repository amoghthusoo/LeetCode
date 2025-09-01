import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        
        intr_classes = []
        for _class in classes:
            a = _class[0]
            b = _class[1]
            d = ((a + 1)/(b + 1)) - (a/b)
            intr_classes.append((-d, a, b))
        
        heapq.heapify(intr_classes)
        

        for _ in range(extraStudents):

            popped = heapq.heappop(intr_classes)
            a = popped[1]
            b = popped[2]

            a += 1
            b += 1
            d = ((a + 1)/(b + 1)) - (a/b)
            heapq.heappush(intr_classes, (-d, a, b))

        ans = 0
        for _class in intr_classes:
            ans += _class[1]/(_class[2] * len(intr_classes))

        return ans

classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4
obj = Solution()
result = obj.maxAverageRatio(classes, extraStudents)
print(result)
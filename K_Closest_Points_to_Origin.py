class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        intr = []

        for point in points:

            d = ((point[0] ** 2) + (point[1] ** 2)) ** 0.5
            intr.append([d, point[0], point[1]])

        intr.sort()

        out = []

        for i in range(k):
            out.append([intr[i][1], intr[i][2]])

        return out
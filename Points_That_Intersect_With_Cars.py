class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        
        distinct_points = set()

        for num in nums:
            distinct_points = distinct_points.union(range(num[0], num[1] + 1))

        return len(distinct_points)
class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        
        intr_ans = 0
        for i in range(len(intervals)):
            for j in range(len(intervals)):

                if(i != j and intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]):
                    intr_ans += 1
                    break
        
        return len(intervals) - intr_ans
    
intervals = [[1,2],[1,4],[3,4]]
obj = Solution()
result = obj.removeCoveredIntervals(intervals)
print(result)

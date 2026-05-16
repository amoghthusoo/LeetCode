class Solution:
    def earliestTime(self, tasks: list[list[int]]) -> int:
        
        ans = int(2 ** 31)
        for task in tasks:
            poss = task[0] + task[1]

            if(poss < ans):
                ans = poss
        return ans
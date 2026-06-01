class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        
        if(len(cost) == 1):
            return cost[0]

        cost.sort(reverse = True)
        ans = 0
        i = 0
        while(i < len(cost)):

            try:
                ans += cost[i]
            except:
                break

            try:
                ans += cost[i + 1]
            except:
                break

            i += 3
        
        return ans

class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        
        twt = 0

        ct = customers[0][0] + customers[0][1]
        twt += ct - customers[0][0]

        i = 1
        while(i < len(customers)):

            if(customers[i][0] <= ct):
                ct += customers[i][1]
            else:
                ct = customers[i][0] + customers[i][1]

            twt += ct - customers[i][0]

            i += 1

        return twt / len(customers)


customers = [[5,2],[5,4],[10,3],[20,1]]
obj = Solution()
out = obj.averageWaitingTime(customers)
print(out)

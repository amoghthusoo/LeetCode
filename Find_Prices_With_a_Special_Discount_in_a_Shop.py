class Solution:
    
    def finalPrices(self, prices: list[int]) -> list[int]:
        
        outList = []

        i = 0
        while(i < len(prices)):

            dicount = 0
            j = i + 1
            while (j < len(prices)):

                if (prices[j] <= prices[i]):
                    dicount = prices[j]
                    break

                j += 1

            outList.append(prices[i] - dicount)
            i += 1

        return outList


prices = [10,1,1,6]
obj = Solution()
solution = obj.finalPrices(prices)
print(solution)

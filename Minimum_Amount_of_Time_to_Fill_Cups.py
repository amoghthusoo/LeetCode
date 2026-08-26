class Solution:
    def fillCups(self, amount: list[int]) -> int:

        ans = 0
        while(sum(amount) != 0):

            amount.sort(reverse = True)

            amount[0] -= 1
            if(amount[1] > 0):
                amount[1] -= 1

            ans += 1

        return ans

amount = [5, 4, 4]
obj = Solution()
result = obj.fillCups(amount)
print(result)
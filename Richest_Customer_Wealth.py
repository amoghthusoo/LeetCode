class Solution:
    def maximumWealth(self, accounts: list) -> int:

        i = 0
        while (i < len(accounts)):

            accounts[i] = sum(accounts[i])
            i += 1

        return max(accounts)

accounts = [[2,8,7],[7,1,3],[1,9,5]]
obj = Solution()
solution = obj.maximumWealth(accounts)
print(solution)

class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        
        intr_arr = []
        intr_arr.append(min(brackets[0][0], income))

        for i in range(1, len(brackets)):

            x = min(brackets[i][0], income) - brackets[i - 1][0]

            if(x >= 0):
                intr_arr.append(x)
            else:
                intr_arr.append(0)

        ans = 0

        for i in range(len(brackets)):
            ans += intr_arr[i] * (brackets[i][1] / 100)
        
        return ans
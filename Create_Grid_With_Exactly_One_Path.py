class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        
        ans = ["." * n]
        temp = "#" * (n - 1) + "."
        for _ in range(m - 1):
            ans.append(temp)
        return ans
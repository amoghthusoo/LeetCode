class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        
        if(m * n != len(original)):
            return []
        
        ans = [[None for _ in range(n)] for _ in range(m)]


        x = 0
        for i in range(m):
            for j in range(n):
                ans[i][j] = original[x]
                x += 1

        return ans
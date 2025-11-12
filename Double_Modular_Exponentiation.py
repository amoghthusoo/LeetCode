class Solution:
    def getGoodIndices(self, variables: list[list[int]], target: int) -> list[int]:
        
        ans = []

        for i in range(len(variables)):

            a = variables[i][0]
            b = variables[i][1]
            c = variables[i][2]
            m = variables[i][3]

            if(pow(pow(a, b, 10), c, m) == target):
                ans.append(i)
        
        return ans
            
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        in_dict = dict()
        out_dict = dict()

        for i in range(1, n + 1):
            in_dict[i] = 0
            out_dict[i] = 0
        
        for edge in trust:
            in_dict[edge[1]] += 1
            out_dict[edge[0]] += 1

        for node, degree in in_dict.items():
            if(degree == n - 1 and out_dict[node] == 0):
                return node
        
        return -1

n = 2
trust = [[1,2]]
obj = Solution()
result = obj.findJudge(n, trust)
print(result)
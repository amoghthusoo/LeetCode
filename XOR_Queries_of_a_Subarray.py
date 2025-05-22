class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        
        prefix_xor = []

        temp_xor = 0
        for e in arr:
            temp_xor ^= e
            prefix_xor.append(temp_xor)
        prefix_xor.append(0)

        ans = []    
        for query in queries:
            ans.append(prefix_xor[query[0] - 1] ^ prefix_xor[query[1]])

        return ans


arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
solution = Solution()
result = solution.xorQueries(arr, queries)
print(result)
class Solution:
    def largestCombination(self, candidates):
        
        inter_result = [0 for _ in range(24)]

        for candidate in candidates:
            bin_str = bin(candidate)[2:].zfill(24)

            for i, digit in enumerate(bin_str):
                if(digit == "1"):
                    inter_result[i] += 1
        
        return max(inter_result)

candidates = [8,8]
solution = Solution()
result = solution.largestCombination(candidates)      
print(result)  
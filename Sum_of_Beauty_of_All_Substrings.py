class Solution:
    def beautySum(self, s: str) -> int:
        
        ans = 0
        for i in range(len(s)):
            temp = 0
            occr_dict = dict()
            for j in range(i, len(s)):
                occr_dict[s[j]] = occr_dict.get(s[j], 0) + 1
                ans += max(occr_dict.values()) - min(occr_dict.values())
        
        return ans
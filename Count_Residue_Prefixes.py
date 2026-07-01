class Solution:
    def residuePrefixes(self, s: str) -> int:
        
        unique_chs = set()
        ans = 0
        
        for i, ch in enumerate(s):
            unique_chs.add(ch)
            if(len(unique_chs) == (i + 1) % 3):
                ans += 1
        
        return ans

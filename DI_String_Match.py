class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        
        m = 0
        M = len(s)

        ans = []

        for ch in s:
            if(ch == "I"):
                ans.append(m)
                m += 1
            else:
                ans.append(M)
                M -= 1
        
        ans.append(m)

        return ans
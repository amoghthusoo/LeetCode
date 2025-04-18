class Solution:

    def encode(self, s):

        out_str = ""

        current_ch = s[0]
        count = 1
        i = 1
        while(i < len(s)):

            if(s[i] == current_ch):
                count += 1
            else:
                out_str += f"{count}{current_ch}"
                current_ch = s[i]
                count = 1

            i += 1

        out_str += f"{count}{current_ch}"
        return out_str
        
    def countAndSay(self, n: int) -> str:
        
        inter_result = "1"

        for _ in range(n - 1):
            inter_result = self.encode(inter_result)
        
        return inter_result


n = 1
solution = Solution()
result = solution.countAndSay(n)
print(result)

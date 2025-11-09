class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        
        s = list(s)

        indices = []
        for i, ch in enumerate(s):
            
            if(ch.isalpha()):
                indices.append(i)

        ans = []

        for i in range(2 ** len(indices)):

            bin_str = bin(i)[2 : ].zfill(len(indices))

            for j in range(len(indices)):
                if(bin_str[j] == "0"):
                    s[indices[j]] = s[indices[j]].lower()
                else:
                    s[indices[j]] = s[indices[j]].upper()

            ans.append("".join(s))
        
        return ans

s = "3z4"
obj = Solution()
result = obj.letterCasePermutation(s)
print(result)

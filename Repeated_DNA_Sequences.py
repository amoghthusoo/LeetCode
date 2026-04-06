class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:

        visisted = set()
        ans = set()
        i = 0
        while(i <= len(s) - 10):
            sub_str = s[i : i + 10]        

            if(sub_str not in visisted):
                visisted.add(sub_str)
            else:
                ans.add(sub_str)
            
            i += 1
        
        return list(ans)

s = "AAAAAAAAAAAAA"
obj = Solution()
result = obj.findRepeatedDnaSequences(s)
print(result)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mappingDict1 : dict = {}
        mappingDict2 : dict = {}

        i = 0
        while (i < len(s)):

            if (s[i] not in mappingDict1):
                mappingDict1[s[i]] = t[i]
            else:

                if (mappingDict1[s[i]] != t[i]):
                    return False
                
            i += 1
        
        j = 0
        while (j < len(t)):

            if (t[j] not in mappingDict2):
                
                mappingDict2[t[j]] = s[j]

            else:

                if (mappingDict2[t[j]] != s[j]):
                    return False
                
            j += 1

        return True

s = "badc"
t = "baba"
obj = Solution()
solution = obj.isIsomorphic(s, t)
print(solution)

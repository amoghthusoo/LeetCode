class Solution:
    def sortVowels(self, s: str) -> str:

        vowels = []
        indices = []

        i = 0
        while(i < len(s)):

            if(s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
                indices.append(i)
                vowels.append(s[i])

            i += 1

        vowels.sort()
        out_str = ""

        i = 0
        while(i < len(s)):

            if(len(indices) != 0 and i == indices[0]):
                indices.pop(0)
                out_str += vowels.pop(0)
            else:
                out_str += s[i]

            i += 1

        return out_str

s = "lYmpH"
obj = Solution()
out = obj.sortVowels(s)
print(out)

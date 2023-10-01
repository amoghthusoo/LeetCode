class Solution:
    def reverseVowels(self, s: str) -> str:

        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowelList = []
        for ch in s:
            if (ch in VOWELS):
                vowelList.append(ch)

        outString = ""

        for ch in s:

            if (ch in VOWELS):
                outString += vowelList.pop()
            else:
                outString += ch

        return outString


s = "leetcode"
obj = Solution()
solution = obj.reverseVowels(s)
print(solution)
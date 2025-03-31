class Solution:
    def makeEqual(self, words: list[str]) -> bool:

        if(len(words) == 1):
            return True

        char_dict = {}

        for word in words:
            for ch in word:
                if(ch not in char_dict):
                    char_dict[ch] = 1
                else:
                    char_dict[ch] += 1

        print(char_dict)

        for e in char_dict.values():
            if(e % len(words) != 0):
                return False
            
        return True
            


words = ["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]
obj = Solution()
out = obj.makeEqual(words)
print(out)

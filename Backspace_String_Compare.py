class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        

        def removeBackspace(s):

            s = list(s)

            while ("#" in s):
                
                hash_index = s.index("#")
                s[hash_index] = None
                if (hash_index - 1 >= 0):
                    s[hash_index - 1] = None

                while (None in s):
                    s.pop(s.index(None))

            return s

        
        s = removeBackspace(s)
        t = removeBackspace(t)

        if (s == t):
            return True
        else:
            return False


s = "a#c"
t = "b"
obj = Solution()
solution = obj.backspaceCompare(s, t)
print(solution)
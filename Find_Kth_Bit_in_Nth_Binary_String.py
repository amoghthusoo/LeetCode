class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        
        def reverse(s):
            return s[-1::-1]


        def invert(s):

            out = ""

            for e in s:
                if(e == "0"):
                    out += "1"
                else:
                    out += "0"
        
            return out

        s = "0"
        for i in range(n - 1):
            s = s + "1" + reverse(invert(s))

        return s[k - 1]

n = 3
k = 1
obj = Solution()
result = obj.findKthBit(n, k)
print(result)

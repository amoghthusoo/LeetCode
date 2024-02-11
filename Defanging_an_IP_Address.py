class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        outStr = ""

        for ch in address:

            if ch == ".":
                outStr += "[.]"
            else:
                outStr += ch

        return outStr

address = "255.100.50.0"
obj = Solution()
solution = obj.defangIPaddr(address)
print(solution)
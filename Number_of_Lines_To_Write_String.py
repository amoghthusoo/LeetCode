class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        
        curr_width = 0
        lines = 0
        
        for ch in s:
            w = widths[ord(ch) - 97]
            if(curr_width + w <= 100):
                curr_width += w
            else:
                curr_width = w
                lines += 1
        
        return [lines + 1, curr_width]

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"
obj = Solution()
result = obj.numberOfLines(widths, s)
print(result)
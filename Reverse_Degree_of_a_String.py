class Solution:
    def reverseDegree(self, s: str) -> int:
        
        reverse_degree = 0
        for i, ch in enumerate(s):
            reverse_degree += (123 - ord(ch)) * (i + 1)
        return reverse_degree

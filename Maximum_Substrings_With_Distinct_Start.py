class Solution:
    def maxDistinct(self, s: str) -> int:
        visited = set()
        for ch in s:
            visited.add(ch)
        return len(visited)

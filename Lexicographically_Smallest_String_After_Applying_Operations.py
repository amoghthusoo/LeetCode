from collections import deque

class Solution:

    def add(self, s, a):

        out = ""
        
        for i, ch in enumerate(s):
            if(i % 2 != 0):
                out += str((int(ch) + a) % 10)
            else:
                out += ch
        
        return out
    
    def rotate(self, s, b):
        
        p1 = s[: b]
        p2 = s[b :]
        return p2 + p1
    

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        queue = deque([s])
        visited = set([s])
        _min = s

        while(len(queue) != 0):
            
            popped = queue.popleft()

            s1 = self.add(popped, a)
            s2 = self.rotate(popped, b)

            if(s1 not in visited):
                visited.add(s1)
                queue.append(s1)

                if(s1 < _min):
                    _min = s1
            
            if(s2 not in visited):
                visited.add(s2)
                queue.append(s2)

                if(s2 < _min):
                    _min = s2

        return _min


s = "0011"
a = 4
b = 2
obj = Solution()
result = obj.findLexSmallestString(s, a, b)
print(result)
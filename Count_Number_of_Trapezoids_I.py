from math import comb

class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        
        mod = int(10 ** 9 + 7)

        freq_dict = dict()

        for point in points:

            if(point[1] not in freq_dict):
                freq_dict[point[1]] = 1
            else:
                freq_dict[point[1]] += 1
        
        for y, freq in freq_dict.items():
            freq_dict[y] = comb(freq, 2)
        
        ans = 0
        ps = 0

        for e in freq_dict.values():
            ans = (ans + e * ps) % mod 
            ps = (ps + e) % mod 
        
        return ans 

points = [[1,0],[2,0],[3,0],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[2,2],[3,2]]
obj = Solution()
result = obj.countTrapezoids(points)
print(result)
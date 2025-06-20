class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
        N = S = E = W = 0

        max_dist = 0
        i = 0
        for e in s:

            if(e == "N"):
                N += 1
            elif(e == "S"):
                S += 1
            elif(e == "E"):
                E += 1
            else:
                W += 1

            q = min(N, S) + min(E, W)

            if(q <= k):
                max_increase = q * 2
            else:
                max_increase = k * 2

            current_dist = abs(N - S) + abs(E - W)

            total_dist = current_dist + max_increase

            if(total_dist > max_dist):
                max_dist = total_dist

        return max_dist
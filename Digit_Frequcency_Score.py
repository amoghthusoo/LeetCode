class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq_map = dict()

        while(n != 0):
            d = n % 10
            freq_map[d] = freq_map.get(d, 0) + 1
            n //= 10

        ans = 0
        for d, f in freq_map.items():
            ans += d * f

        return ans 
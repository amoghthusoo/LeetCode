from collections import Counter

class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 0
        for i in range(n + 1):
            if(len(Counter(bin(i)[2 : ])) == 1):
                ans += 1
        return ans
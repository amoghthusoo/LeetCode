from collections import Counter

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:

        freq_dict = Counter(str(n))

        _min = min(freq_dict.values()) 

        poss_ans = []

        for d, f in freq_dict.items():

            if(f == _min):
                poss_ans.append(d)

        poss_ans.sort()

        return int(poss_ans[0])


n = 1553322
obj = Solution()
result = obj.getLeastFrequentDigit(n)
print(result)

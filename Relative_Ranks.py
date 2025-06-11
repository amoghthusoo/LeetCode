class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        
        rank_dict = {}
        sorted_score = sorted(score, reverse=True)

        rank_dict = {}

        try:
            rank_dict[sorted_score.pop(0)] = "Gold Medal"
            rank_dict[sorted_score.pop(0)] = "Silver Medal"
            rank_dict[sorted_score.pop(0)] = "Bronze Medal"
        except:
            pass
        
        i = 4
        for s in sorted_score:
            rank_dict[s] = str(i)
            i += 1

        out = []
        for s in score:
            out.append(rank_dict[s])

        return out

score = [10,3,8,9,4]
obj = Solution()
out = obj.findRelativeRanks(score)
print(out)
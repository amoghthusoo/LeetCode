class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        
        occr_dict = dict()
        count = 0

        for d in dominoes:
            if(tuple(d) in occr_dict):
                count += occr_dict[tuple(d)]
            
            if(d[0] != d[1]):

                d.reverse()

                if(tuple(d) in occr_dict):
                    count += occr_dict[tuple(d)]

                d.reverse()

            if(tuple(d) not in occr_dict):
                occr_dict[tuple(d)] = 1
            else:
                occr_dict[tuple(d)] += 1

        return count

dominoes = [[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]
solution = Solution()
result = solution.numEquivDominoPairs(dominoes)
print(result)
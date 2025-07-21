class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        
        i = 0
        while(i < len(score)):

            j = 0
            while(j < len(score) - 1 - i):

                if(score[j][k] < score[j + 1][k]):
                    score[j], score[j + 1] = score[j + 1], score[j]

                j += 1
            i += 1

        return score
    
score = [[3,4],[5,6]]
k = 0
obj = Solution()
out = obj.sortTheStudents(score, k)
print(out)

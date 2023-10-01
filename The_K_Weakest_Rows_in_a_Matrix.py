class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        
        no_of_soldiers = []

        i = 0
        while(i < len(mat)):

            no_of_soldiers.append(mat[i].count(1))
            i += 1

        no_of_soldiers_sorted = sorted(no_of_soldiers)
        
        interList = []
        i = 0
        while(i < len(no_of_soldiers_sorted)):
            
            interList.append(no_of_soldiers.index(no_of_soldiers_sorted[i]))
            no_of_soldiers[no_of_soldiers.index(no_of_soldiers_sorted[i])] = None

            i += 1

        return interList[0 : k]


mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2
obj = Solution()
solution = obj.kWeakestRows(mat, k)
print(solution)
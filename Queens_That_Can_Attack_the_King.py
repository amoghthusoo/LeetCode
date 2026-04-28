class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:

        queen_set = set()

        for queen in queens:
            queen_set.add((queen[0], queen[1]))

        ans = []

        i = king[0]
        j = king[1]

        while(i >= 0 and j >= 0):

            if((i, j) in queen_set):
                ans.append([i, j])
                break
            
            i -= 1
            j -= 1
        
        i = king[0]
        j = king[1]

        while(i >= 0):

            if((i, j) in queen_set):
                ans.append([i, j])
                break
            
            i -= 1
        
        i = king[0]
        j = king[1]

        while(i >= 0 and j < 8):

            if((i, j) in queen_set):
                ans.append([i, j])
                break
            
            i -= 1
            j += 1

        i = king[0]
        j = king[1]

        while(j >= 0):

            if((i, j) in queen_set):
                ans.append([i, j])
                break
            
            j -= 1

        i = king[0]
        j = king[1]

        while(j < 8):

            if((i, j) in queen_set):
                ans.append([i, j])
                break
            
            j += 1
        
        i = king[0]
        j = king[1]

        while(i < 8 and j >= 0):

            if((i, j) in queen_set):
                ans.append([i, j])
                break
            
            i += 1
            j -= 1
        
        i = king[0]
        j = king[1]

        while(i < 8):

            if((i, j) in queen_set):
                ans.append([i, j])
                break
            
            i += 1

        i = king[0]
        j = king[1]

        while(i < 8 and j < 8):

            if((i, j) in queen_set):
                ans.append([i, j])
                break
            
            i += 1
            j += 1

        return ans
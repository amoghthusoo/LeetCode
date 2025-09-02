class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        count = 0
        
        i = 0
        while(i < len(points)):

            j = 0
            while(j < len(points)):

                if(i != j):

                    x1 = points[i][0]
                    y1 = points[i][1]

                    x2 = points[j][0]
                    y2 = points[j][1]

                    if(x1 <= x2 and y1 >= y2):

                        k = 0
                        while(k < len(points)):

                            if(k != i and k != j):
                                
                                x = points[k][0]
                                y = points[k][1]

                                if(x1 <= x and x <= x2 and y2 <= y and y <= y1):
                                    break

                            k += 1
                        
                        else:
                            count += 1


                j += 1
            i += 1
    
        return count

points = [[3,1],[1,3],[1,1]]
obj = Solution()
result = obj.numberOfPairs(points)
print(result)
class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:

        ans = []

        for i in range(len(img)):
            temp = []
            for j in range(len(img[0])):

                total = img[i][j]
                count = 1

                if(i - 1 >= 0 and j - 1 >= 0):
                    total += img[i - 1][j - 1]
                    count += 1
                
                if(i - 1 >= 0):
                    total += img[i - 1][j]
                    count += 1
                
                if(i - 1 >= 0 and j + 1 < len(img[0])):
                    total += img[i - 1][j + 1]
                    count += 1

                if(j - 1 >= 0):
                    total += img[i][j - 1]
                    count += 1
                
                if(j + 1 < len(img[0])):
                    total += img[i][j + 1]
                    count += 1

                if(i + 1 < len(img) and j - 1 >= 0):
                    total += img[i + 1][j - 1]
                    count += 1
                
                if(i + 1 < len(img)):
                    total += img[i + 1][j]
                    count += 1
                
                if(i + 1 < len(img) and j + 1 < len(img[0])):
                    total += img[i + 1][j + 1]
                    count += 1
                
                temp.append(total // count)

            ans.append(temp)

        return ans
    
img = [[100,200,100],[200,50,200],[100,200,100]]
obj = Solution()
result = obj.imageSmoother(img)
print(result)
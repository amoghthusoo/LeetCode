class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        
        i = 0
        while (i < len(image)):

            image[i].reverse()

            j = 0
            while (j < len(image[i])):

                if (image[i][j] == 0):
                    image[i][j] = 1
                else:
                    image[i][j] = 0

                j += 1

            i += 1
        
        return image



image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
obj = Solution()
solution = obj.flipAndInvertImage(image)
print(solution)
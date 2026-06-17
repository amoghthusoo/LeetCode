class Solution:

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        
        def fill(image, r, c, source_color, target_color):
            
            if(image[r][c] == source_color):
                image[r][c] = color

                if(c > 0):
                    fill(image, r, c - 1, source_color, target_color)
                
                if(c < len(image[0]) - 1):
                    fill(image, r, c + 1, source_color, target_color)
                
                if(r > 0):
                    fill(image, r - 1, c, source_color, target_color)
                
                if(r < len(image) - 1):
                    fill(image, r + 1, c, source_color, target_color)
                
        if(image[sr][sc] != color):
            fill(image, sr, sc, image[sr][sc], color)
        return image
    
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
obj = Solution()
result = obj.floodFill(image, sr, sc, color)
print(result)

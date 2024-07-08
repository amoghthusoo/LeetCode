class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:


        if(len(flowerbed) == 1 and flowerbed[0] == 0 and n <= 1):
            return True
        
        count = 0

        i = 0
        while(i < len(flowerbed)):

            if(i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1

            elif(i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0):
                flowerbed[i] = 1
                count += 1

            elif(flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1


            if(count >= n):
                return True


            i += 1

        return False
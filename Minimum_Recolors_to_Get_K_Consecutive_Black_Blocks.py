class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = j = 0

        min_black_count = -1
        black_count = 0

        for _ in range(k):
            if(blocks[j] == "W"):
                black_count += 1
            j += 1

        min_black_count = black_count
        j -= 1

        while(True):

            j += 1
            if(j == len(blocks)):
                return min_black_count

            if(blocks[j] == "W"):
                black_count += 1
            
            if(blocks[i] == "W"):
                black_count -= 1

            i += 1

            if(black_count < min_black_count):
                min_black_count = black_count
        
        return min_black_count
            

blocks = "WBBWWBBWBW"
k = 7

obj = Solution()
result = obj.minimumRecolors(blocks, k)
print(result)

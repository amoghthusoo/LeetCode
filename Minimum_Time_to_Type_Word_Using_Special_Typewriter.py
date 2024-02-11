class Solution:
    def minTimeToType(self, word: str) -> int:
        
        def min_time_to_move(from_ch, to_ch):
            t1 = abs(ord(from_ch) - ord(to_ch))
            t2 = 26 - t1
            return min(t1, t2)


        total_time = 0
        total_time += min_time_to_move('a', word[0])
        total_time += 1        
        i = 0
        while(i < len(word) - 1):
            
        
            total_time += min_time_to_move(word[i], word[i + 1])

            total_time += 1
            i += 1

        return total_time


word = "zjpc"
obj = Solution()
solution = obj.minTimeToType(word)
print(solution)
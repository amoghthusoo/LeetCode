class Solution:
    def memLeak(self, memory1: int, memory2: int) -> list[int]:

        i = 1

        while(i <= memory1 or i <= memory2):

            if(memory2 > memory1):
                memory2 -= i
            else:
                memory1 -= i
        
            i += 1

        return [i, memory1, memory2]

memory1 = 8
memory2 = 11
obj = Solution()
result = obj.memLeak(memory1, memory2)
print(result)
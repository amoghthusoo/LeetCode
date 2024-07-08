class Solution:
    def isFascinating(self, n: int) -> bool:
        
        concat_str = str(n) + str(2 * n) + str(3 * n)

        if(len(concat_str) != 9):
            return False

        i = 1
        while(i <= 9):

            if(str(i) not in concat_str):
                return False

            i += 1

        return True
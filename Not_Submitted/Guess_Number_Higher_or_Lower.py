# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:

        lower_limit = 1
        upper_limit = n

        while(True):

            guess_num = (lower_limit + upper_limit) // 2

            hint = guess(guess_num)

            if(hint == 0):
                return guess_num

            elif(hint == 1):
                lower_limit = guess_num + 1

            elif(hint == -1):
                upper_limit = guess_num - 1

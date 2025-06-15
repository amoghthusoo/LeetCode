class Solution:
    def maxDiff(self, num: int) -> int:

        non_nine_digit = None

        for e in str(num):

            if(e != "9"):
                non_nine_digit = e
                break
        
        if(non_nine_digit == None):
            max_num = num
        else:
            max_num = str(num).replace(non_nine_digit, "9")

        non_zero_one_digit = None

        if(str(num)[0] != "1"):
            non_zero_one_digit = str(num)[0]
            min_num = str(num).replace(non_zero_one_digit, "1")

        else:
            for e in str(num):

                if(e not in ["0", "1"]):
                    non_zero_one_digit = e
                    break
            
            if(non_zero_one_digit == None):
                min_num = str(num)
            else:
                min_num = str(num).replace(non_zero_one_digit, "0")

        return int(max_num) - int(min_num)
        
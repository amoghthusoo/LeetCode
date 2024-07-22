class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        max_zero_count = 0
        max_one_count = 0

        previous_bit = s[0]

        count = 1

        i = 1
        while(i < len(s)):

            if(s[i] == previous_bit):
                count += 1

            else:

                if(previous_bit == "0"):

                    if(count > max_zero_count):
                        max_zero_count = count

                else:

                    if(count > max_one_count):
                        max_one_count = count

                count = 1
                previous_bit = s[i]

            i += 1

        if(previous_bit == "0"):

            if(count > max_zero_count):
                max_zero_count = count

        else:

            if(count > max_one_count):
                max_one_count = count

        
        # print(max_one_count)
        # print(max_zero_count)

        if(max_one_count > max_zero_count):
            return True
        else:
            return False
        
s = "110100010"
obj = Solution()
out = obj.checkZeroOnes(s)
print(out)
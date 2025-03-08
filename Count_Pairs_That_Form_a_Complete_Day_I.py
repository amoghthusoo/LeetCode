class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        
        count = 0

        i = 0
        while(i < len(hours) - 1):

            j = i + 1
            while(j < len(hours)):

                if((hours[i] + hours[j]) % 24 == 0):
                    count += 1

                j += 1
            i += 1

        return count
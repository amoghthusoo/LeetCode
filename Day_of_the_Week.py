class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        day_dict = {
            0 : "Sunday",
            1 : "Monday", 
            2 : "Tuesday",
            3 : "Wednesday",
            4 : "Thursday",
            5 : "Friday",
            6 : "Saturday"
        }
        
        if(month not in [1, 2]):
            m = month - 2
        
        elif (month == 1):
            m = 11
            year -= 1

        elif (month == 2):
            m = 12
            year -= 1

        k = day
        C = int(str(year)[0:2])
        D = int(str(year)[2:4])

        F = k + ((13 * m - 1) // 5) + D + (D // 4) + (C // 4) - 2 * C
        day_num = F % 7

        return day_dict[day_num]

    
day = 15
month = 8
year = 1993
obj = Solution()
out = obj.dayOfTheWeek(day, month, year)
print(out)

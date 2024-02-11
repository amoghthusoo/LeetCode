class Solution:
    def dayOfYear(self, date: str) -> int:
        
        _date = 1
        month = 1
        year = int(date[0:4])

        current_date = int(date[8:10])
        current_month = int(date[5:7])
        current_year = int(date[0:4])

        date_list = [_date, month, year]
        current_date_list = [current_date, current_month, current_year]

        age_in_days = 0

        while True:

            if (date_list[0] == current_date_list[0] and
                date_list[1] == current_date_list[1] and
                    date_list[2] == current_date_list[2]):

                break

            date_list[0] += 1

            if (date_list[1] in [1, 3, 5, 7, 8, 10, 12] and date_list[0] == 32):
                date_list[0] = 1
                date_list[1] += 1

            elif (date_list[1] in [4, 6, 9, 11] and date_list[0] == 31):
                date_list[0] = 1
                date_list[1] += 1

            elif (date_list[1] == 2 and date_list[2] % 4 != 0 and date_list[0] == 29):

                date_list[0] = 1
                date_list[1] += 1

            elif (date_list[1] == 2 and date_list[2] % 4 == 0 and date_list[2] % 100 != 0 and date_list[0] == 30):

                date_list[0] = 1
                date_list[1] += 1

            elif (date_list[1] == 2 and date_list[2] % 100 == 0):

                if (date_list[2] % 400 == 0 and date_list[0] == 30):
                    date_list[0] = 1
                    date_list[1] += 1

                elif (date_list[2] % 400 != 0 and date_list[0] == 29):
                    date_list[0] = 1
                    date_list[1] += 1

            if (date_list[1] == 13):
                date_list[1] = 1
                date_list[2] += 1

            age_in_days += 1

        return age_in_days + 1

date = "2019-01-09"
obj = Solution()
solution = obj.dayOfYear(date)
print(solution)
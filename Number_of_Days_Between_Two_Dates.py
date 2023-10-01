class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        if (int(date1[0:4]) > int(date2[0:4])):
            recent_date = date1
            past_date = date2
        elif((int(date1[0:4]) == int(date2[0:4])) and (int(date1[5:7]) > int(date2[5:7]))):
            recent_date = date1
            past_date = date2
        elif((int(date1[0:4]) == int(date2[0:4])) and (int(date1[5:7]) == int(date2[5:7])) and (int(date1[8:10]) > int(date2[8:10]))):
            recent_date = date1
            past_date = date2
        else:
            recent_date = date2
            past_date = date1
        
        
        _date = int(past_date[8:10])
        month = int(past_date[5:7])
        year = int(past_date[0:4])

        current_date = int(recent_date[8:10])
        current_month = int(recent_date[5:7])
        current_year = int(recent_date[0:4])

        date_list = [_date, month, year]
        current_date_list = [current_date, current_month, current_year]

        no_of_days = 0

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

            no_of_days += 1

        return no_of_days 


date1 = "2019-06-29"
date2 = "2019-06-30"
obj = Solution()
solution = obj.daysBetweenDates(date1, date2)
print(solution)
class Solution:
    def reformatDate(self, date: str) -> str:
        
        month_dict = {"Jan" : "01", 
                      "Feb" : "02", 
                      "Mar" : "03", 
                      "Apr" : "04", 
                      "May" : "05", 
                      "Jun" : "06", 
                      "Jul" : "07", 
                      "Aug" : "08", 
                      "Sep" : "09", 
                      "Oct" : "10", 
                      "Nov" : "11", 
                      "Dec" : "12"}

        date = date.split()
        
        d = date[0][0:-2]
        if(len(d) == 1):
            d = "0" + d
        m = month_dict[date[1]]
        y = date[2]

        return y + "-" + m + "-" + d
    

        

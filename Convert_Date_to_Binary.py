class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        date_arr = date.split("-")
        result = ""
        result += bin(int(date_arr[0]))[2:] + "-" + bin(int(date_arr[1]))[2:] + "-" + bin(int(date_arr[2]))[2:]
        
        return result
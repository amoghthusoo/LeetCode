class Solution:
    def intToRoman(self, num: int) -> str:
        
        ones_dict = {
            "0" : "",
            "1" : "I",
            "2" : "II",
            "3" : "III",
            "4" : "IV",
            "5" : "V",
            "6" : "VI",
            "7" : "VII",
            "8" : "VIII",
            "9" : "IX"
        }

        tens_dict = {
            "0" : "",
            "1" : "X",
            "2" : "XX",
            "3" : "XXX",
            "4" : "XL",
            "5" : "L",
            "6" : "LX",
            "7" : "LXX",
            "8" : "LXXX",
            "9" : "XC",
        }

        hundreds_dict = {
            "0" : "",
            "1" : "C",
            "2" : "CC",
            "3" : "CCC",
            "4" : "CD",
            "5" : "D",
            "6" : "DC",
            "7" : "DCC",
            "8" : "DCCC",
            "9" : "CM",
        }

        thousands_dict = {
            "1" : "M",
            "2" : "MM",
            "3" : "MMM",
        }


        ans = []
        num = str(num)

        try:
            ans.insert(0, ones_dict[num[-1]])
        except:
            pass
        
        try:
            ans.insert(0, tens_dict[num[-2]])
        except:
            pass
        
        try:
            ans.insert(0, hundreds_dict[num[-3]])
        except:
            pass
        
        try:
            ans.insert(0, thousands_dict[num[-4]])
        except:
            pass

        return "".join(ans)
    
num = 1994
obj = Solution()
result = obj.intToRoman(num)
print(result)
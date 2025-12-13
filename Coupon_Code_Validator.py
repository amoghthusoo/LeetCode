class Solution:

    def __init__(self):
        capital_char = [chr(i) for i in range(65, 92)]
        small_char = [chr(i) for i in range(97, 124)]
        digits = [str(i) for i in range(10)]

        self.valid_chars = set(capital_char + small_char + digits + ["_"])
        self.valid_buisnesses = {"electronics", "grocery", "pharmacy", "restaurant"}

    def check_valid_str(self, s):

        if(not s):
            return False

        for ch in s:
            if(ch not in self.valid_chars):
                return False
        
        return True
    
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        
        inter_ans = {
            "electronics" : [],
            "grocery" : [],
            "pharmacy" : [],
            "restaurant" : [],
        }

        for i in range(len(code)):
            
            if(self.check_valid_str(code[i]) and businessLine[i] in self.valid_buisnesses and isActive[i]):
                inter_ans[businessLine[i]].append(code[i])

        
        ans = []
        for key, val in inter_ans.items():
            ans.extend(sorted(val))
        
        return ans
    
code = ["SAVE20","","PHARMA5","SAVE@20"]
businessLine = ["restaurant","grocery","pharmacy","restaurant"]
isActive = [True,True,True,True]
obj = Solution()
result = obj.validateCoupons(code, businessLine, isActive)
print(result)
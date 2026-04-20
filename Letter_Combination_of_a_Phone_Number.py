class Solution:

    def __init__(self):

        self.button_dict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

    def generate_comb(self, num_str):
        
        if(len(num_str) == 0):
            return [""]

        ans = []
        first_ch = num_str[0]
        remaining_str = num_str[1 : ]
        correponding_str = self.button_dict[first_ch]
        
        concat_arr = self.generate_comb(remaining_str)

        for ch in correponding_str:
            for s in concat_arr:
                ans.append(ch + s)
        
        return ans
        

    def letterCombinations(self, digits: str) -> list[str]:
        ans = self.generate_comb(digits)
        if(ans == [""]):
            return []
        else:
            return ans
    
digits = ""
obj = Solution()
result = obj.letterCombinations(digits)
print(result)
        
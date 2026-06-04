class Solution:
    def reformat(self, s: str) -> str:
        
        letters = []
        digits = []
        for ch in s:
            if(ch.isalpha()):
                letters.append(ch)
            else:
                digits.append(ch)
        
        if(abs(len(letters) - len(digits)) > 1):
            return ""
        
        if(len(letters) >= len(digits)):
            larger = letters
            smaller = digits
        else:
            larger = digits
            smaller = letters

        ans = []
        i = 0
        while(i < len(smaller)):
            ans.append(larger[i])
            ans.append(smaller[i])
            i += 1
        
        try:
            ans.append(larger[i])
        except:
            pass
        return ans
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        s1_even = dict()
        s1_odd = dict()
        s2_even = dict()
        s2_odd = dict()

        for i, ch in enumerate(s1):

            if(i % 2 == 0):
                s1_even[ch] = s1_even.get(ch, 0) + 1
            else:
                s1_odd[ch] = s1_odd.get(ch, 0) + 1
        
        for i, ch in enumerate(s2):

            if(i % 2 == 0):
                s2_even[ch] = s2_even.get(ch, 0) + 1
            else:
                s2_odd[ch] = s2_odd.get(ch, 0) + 1

        if(s1_even == s2_even and s1_odd == s2_odd):
            return True
        
        return False

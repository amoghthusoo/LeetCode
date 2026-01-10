from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2)

        if(c1 == c2):
            
            cnt = 0
            i = 0
            while(i < len(s1)):

                if(s1[i] != s2[i]):
                    cnt += 1    

                i += 1

            if(cnt <= 2):
                return True
            
            else:
                return False

        else:
            return False
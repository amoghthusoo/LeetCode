class Solution:
    def countValidPrefixes(self, s: str) -> int:

        ans = 0
        zero_cnt = 0
        one_cnt = 0

        i = 0 
        while(i < len(s)):

            if(s[i] == "0"):
                zero_cnt += 1
            else:
                one_cnt += 1

            if(abs(zero_cnt - one_cnt) <= 1):
                ans += 1

            i += 1

        return ans
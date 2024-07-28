class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        if(s[0] == 'R'):
            first_char = 'R'
            second_char = 'L'

        else:

            first_char = 'L'
            second_char = 'R'

        ans = 0
        count = 0

        for e in s:

            if(e == first_char):
                count += 1

            else:
                count -= 1

            if(count == 0):
                ans += 1

        return ans
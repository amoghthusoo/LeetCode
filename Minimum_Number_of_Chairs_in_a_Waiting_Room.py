class Solution:
    def minimumChairs(self, s: str) -> int:
        
        count = 0
        ans = -1

        for e in s:

            if(e == 'E'):
                count += 1
            else:
                count -= 1

            if(count > ans):
                ans = count

        return ans
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        freq_dict = Counter(s)

        even = []
        odd = []

        for e in freq_dict.values():
            if(e % 2 == 0):
                even.append(e)
            else:
                odd.append(e)
        
        odd.sort()
        ans = sum(even)
        try:
            ans += odd.pop(0)
        except:
            pass
        
        k = len(odd)
        ans += sum(odd)
        ans -= k

        return ans


s = "abccccdd"
obj = Solution()
result = obj.longestPalindrome(s)
print(result)
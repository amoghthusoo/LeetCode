class Solution:
    def largestInteger(self, num: int) -> int:
        
        num = str(num)
        even = []
        odd = []

        for d in num:

            if(int(d) % 2 == 0):
                even.append(d)
            else:
                odd.append(d)
        
        even.sort(reverse = True)
        odd.sort(reverse = True)

        ans = ""

        i = 0
        while(i < len(num)):

            if(int(num[i]) % 2 == 0):
                ans += even.pop(0)
            else:
                ans += odd.pop(0)

            i += 1

        return int(ans)

num = 65875
obj = Solution()
result = obj.largestInteger(num)
print(result)
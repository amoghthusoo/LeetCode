class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        count = 0
        for num in range(low, high + 1):
            
            num = str(num)  

            if(len(num) % 2 != 0):
                continue

            n = len(num) // 2
            left_sum = 0
            for i in range(n):
                left_sum += int(num[i])
            
            right_sum = 0
            for i in range(n, len(num)):
                right_sum += int(num[i])

            if(left_sum == right_sum):
                count += 1
        
        return count

low = 1200
high = 1230
solution = Solution()
result = solution.countSymmetricIntegers(low, high)
print(result)
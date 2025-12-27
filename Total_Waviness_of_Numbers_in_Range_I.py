class Solution:

    def count_waviness(self, n):
        n = str(n)

        if(len(n) in {1, 2}):
            return 0
        
        cnt = 0
        i = 1
        while(i < len(n) - 1):
            
            if((n[i] > n[i - 1] and n[i] > n[i + 1]) or (n[i] < n[i - 1] and n[i] < n[i +1])):
                cnt += 1

            i += 1
        
        return cnt

    def totalWaviness(self, num1: int, num2: int) -> int:
        
        ans = 0
        i = num1
        while(i <= num2):
            ans += self.count_waviness(i)
            i += 1
        
        return ans 

num1 = 4848
num2 = 4848
obj = Solution()
result = obj.totalWaviness(num1, num2)
print(result)
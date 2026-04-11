class Solution:
    def countPrimes(self, n: int) -> int:
        
        if(n < 2):
            return 0
        
        bool_arr = [False for _ in range(n)]

        for i in range(2, n):

            if(not bool_arr[i]):

                multiple = i
                multiple += i
                while(multiple < n):
                    bool_arr[multiple] = True
                    multiple += i
        
        return bool_arr.count(False) - 2

n = 10
obj = Solution()
result = obj.countPrimes(n)
print(result)
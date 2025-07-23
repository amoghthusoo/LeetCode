class Solution:
    def pow(self, x, n):

        if(n == 0):
            return 1
            
        exp_arr = [n]
        exp = n
        while(exp != 1):
            exp //= 2
            exp_arr.append(exp)

        dp = {1 : x}

        i = len(exp_arr) - 2
        while(i >= 0):

            if(exp_arr[i] % 2 == 0):
                dp[exp_arr[i]] = dp[exp_arr[i]//2] * dp[exp_arr[i]//2]
            else:
                dp[exp_arr[i]] = x * dp[exp_arr[i]//2] * dp[exp_arr[i]//2]

            i -= 1

        return dp[n]

    def myPow(self, x: float, n: int) -> float:

        p = self.pow(x, abs(n))

        if(n <= 0):
            return 1 / p
        else:
            return p
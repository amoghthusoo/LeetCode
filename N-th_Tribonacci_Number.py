class Solution:
    def tribonacci(self, n: int) -> int:
        
        if(n == 0):
            return 0
        elif(n == 1):
            return 1
        elif(n == 2):
            return 1

        arr = [None for _ in range(n + 1)]
        arr[0] = 0
        arr[1] = 1
        arr[2] = 1

        for i in range(3, len(arr)):
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
        
        return arr[n]

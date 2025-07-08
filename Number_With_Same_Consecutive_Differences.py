class Solution:

    def __init__(self):
        self.n = None
        self.k = None
        self.ans = set()

    def construct_num(self, num):

        if(len(num) == self.n):
            self.ans.add(int(num))
            return
        
        last_digit = int(num[-1])

        if(last_digit + self.k < 10):
            self.construct_num(num + str(last_digit + self.k))

        if(last_digit - self.k >= 0):
            self.construct_num(num + str(last_digit - self.k))


    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        self.n = n
        self.k = k

        for i in range(1, 10):
            self.construct_num(str(i))

        return list(self.ans)        
    
n = 2
k = 1
obj = Solution()
result = obj.numsSameConsecDiff(n, k)
print(result)

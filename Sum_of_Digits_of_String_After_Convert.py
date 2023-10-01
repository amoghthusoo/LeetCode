class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def letterToPosition(ch : str) -> int:
            return ord(ch) - 96
        
        def digitStrSum(s : str) -> int:

            total = 0
            for digit in s:
                total += int(digit)
            return total
                
        digitStr = ""

        for ch in s:
            digitStr += str(letterToPosition(ch))

        total = 0
        counter = 1

        while True:

            total = digitStrSum(digitStr)
            if (counter == k):
                break
            digitStr = str(total)
            counter += 1
        
        return total



s = 'zbax'
k = 2
obj = Solution()
solution = obj.getLucky(s, k)
print(solution)
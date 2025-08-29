class Solution:

    def get_even_odd_count(self, n):

        if(n % 2 == 0):
            even_count = (n - 2) // 2 + 1
            odd_count = n - even_count
        else:
            odd_count = (n - 1) // 2 + 1
            even_count = n - odd_count
        
        return even_count, odd_count

    def flowerGame(self, n: int, m: int) -> int:
        
        even1, odd1 = self.get_even_odd_count(n)
        even2, odd2 = self.get_even_odd_count(m)

        return even1 * odd2 + even2 * odd1

n = 1
m = 1
obj = Solution()
result = obj.flowerGame(n, m)
print(result)
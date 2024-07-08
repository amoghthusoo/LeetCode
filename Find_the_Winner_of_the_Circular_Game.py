class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        friend_list = list(range(1, n + 1))

        i = 0
        while(len(friend_list) != 1):
            
            count = 1
            while(count != k):
                i = (i + 1) % len(friend_list)
                count += 1

            friend_list.pop(i)

        return friend_list[0]
    
n = 6
k = 5
obj = Solution()
out = obj.findTheWinner(n, k)
print(out)
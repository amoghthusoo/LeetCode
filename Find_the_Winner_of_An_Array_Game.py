from collections import deque

class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:

        if(k >= len(arr)):
            return max(arr)

        dq = deque(arr)
        win_count = dict()

        while(True):

            first = dq.popleft()
            second = dq.popleft()

            if(first > second):

                if(first not in win_count):
                    win_count[first] = 1
                else:
                    win_count[first] += 1

                if(win_count[first] == k):
                    return first

                dq.appendleft(first)
                dq.append(second)

            else:

                if(second not in win_count):
                    win_count[second] = 1
                else:
                    win_count[second] += 1

                if(win_count[second] == k):
                    return second

                dq.appendleft(second)
                dq.append(first)

arr = [3,2,1]
k = 10
obj = Solution()
result = obj.getWinner(arr, k)
print(result)        
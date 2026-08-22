class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        curr = 0
        ans = 0
        for request in requests:
            ans += abs(request - curr)
            curr = request

        return ans
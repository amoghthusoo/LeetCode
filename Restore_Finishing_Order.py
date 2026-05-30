class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        
        friends = set(friends)

        ans = []
        for e in order:
            if(e in friends):
                ans.append(e)
        return ans
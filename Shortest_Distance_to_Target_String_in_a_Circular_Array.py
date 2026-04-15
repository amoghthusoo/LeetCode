class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        
        i = startIndex
        cnt = 0
        ans1 = None
        for _ in range(len(words)):
            if(words[i] == target):
                ans1 = cnt
            else:
                cnt += 1
                i = (i + 1) % len(words)
        
        if(ans1 == None):
            return -1

        i = startIndex
        cnt = 0
        ans2 = None
        for _ in range(len(words)):
            if(words[i] == target):
                ans2 = cnt
            else:
                cnt += 1
                i = (i - 1) % len(words)
        
        return min(ans1, ans2)
    




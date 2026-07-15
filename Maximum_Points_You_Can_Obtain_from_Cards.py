class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:

        if(k == len(cardPoints)):
            return sum(cardPoints)

        left_sum = 0
        for i in range(k):
            left_sum += cardPoints[i]
        
        right_sum = 0
        ans = left_sum

        i = k - 1
        j = len(cardPoints) - 1
        while(i >= 0):

            left_sum -= cardPoints[i]
            right_sum += cardPoints[j]
            i -= 1
            j -= 1
            ans = max(ans, left_sum + right_sum)
        
        return ans

cardPoints = [1,2,3,4,5,6,1]
k = 3
obj = Solution()
result = obj.maxScore(cardPoints, k)
print(result)
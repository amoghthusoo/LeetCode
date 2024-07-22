class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        
        divisibility_score = {}

        for divisor in divisors:

            divisibility_score[divisor] = 0

            for num in nums:

                if(num % divisor == 0):

                    divisibility_score[divisor] += 1
        
        max_score = max(divisibility_score.values())
        min_divisor = 2 ** 31
        for key, value in divisibility_score.items():

            if(value == max_score):

                if(key < min_divisor):
                    min_divisor = key

        return min_divisor            

nums = [20,14,21,10]
divisors = [10,16,20]
obj = Solution()
out = obj.maxDivScore(nums, divisors)
print(out)
from collections import Counter
class Solution:
    def numberOfPairs(self, nums: list) -> list:
        
        numberOfPairs = 0
        leftOverIntegers = 0
        occDict = dict(Counter(nums))

        for num in list(occDict.values()):

            numberOfPairs += num // 2
            leftOverIntegers += num % 2

        return [numberOfPairs, leftOverIntegers]

nums = [1,1]
obj = Solution()
solution = obj.numberOfPairs(nums)
print(solution)
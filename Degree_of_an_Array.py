from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:

        occr_dict = Counter(nums)
        max_freq = max(occr_dict.values())
        intr_nums = []

        for num, freq in occr_dict.items():
            if(freq == max_freq):
                intr_nums.append(num)

        revr_nums = nums[-1::-1]

        ans = float("inf")
        for num in intr_nums:
            start = nums.index(num)
            end = len(nums) -1 - revr_nums.index(num)
            diff = end - start + 1
            ans = min(ans, diff)

        return ans

def main():
    nums = [1,2,2,3,1]
    obj = Solution()
    result = obj.findShortestSubArray(nums)
    print(result)

if(__name__ == "__main__"):
    main()
    
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            prod = 1
            _lcm = nums[i]
            _gcd = nums[i]
            for j in range(i, len(nums)):
                prod *= nums[j]
                _lcm = lcm(_lcm, nums[j])
                _gcd = gcd(_gcd, nums[j])

                if(prod == _lcm * _gcd):
                    ans = max(ans, j - i + 1)

        return ans
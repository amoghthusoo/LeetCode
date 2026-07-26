class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:

        ans = 0
        i = 0
        while(i < len(nums)):

            j = i + 1
            while(j < len(nums)):

                k = j + 1
                while(k < len(nums)):

                    l = k + 1
                    while(l < len(nums)):

                        if(nums[i] + nums[j] + nums[k] == nums[l]):
                            ans += 1

                        l += 1
                    k += 1
                j += 1
            i += 1

        return ans
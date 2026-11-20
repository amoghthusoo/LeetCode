class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        faster = nums[0]
        slower = nums[0]


        faster = nums[nums[faster]]
        slower = nums[slower]
       
        while(slower != faster):
        
            faster = nums[nums[faster]]
            slower = nums[slower]

        slower = nums[0]
        while(slower != faster):

            faster = nums[faster]
            slower = nums[slower]

        return faster
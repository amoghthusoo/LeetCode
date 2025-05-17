class Solution:
    def countElements(self, nums: list[int]) -> int:
        
        count = 0

        for num in nums:

            smaller = False
            larger = False

            for n in nums:
                if(n > num):
                    larger = True
                    break
            
            for n in nums:
                if(n < num):
                    smaller = True
                    break

            if(smaller and larger):
                count += 1

        return count
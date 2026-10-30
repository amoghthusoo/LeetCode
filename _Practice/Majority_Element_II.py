class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        occDict : dict = dict(Counter(nums))
        ansList = []
        for key in occDict:

            if (occDict[key] > floor(len(nums)/3)):
                ansList.append(key)

        return ansList
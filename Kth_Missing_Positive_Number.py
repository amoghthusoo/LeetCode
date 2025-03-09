class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        
        num_dict = {}
        for num in arr:
            num_dict[num] = None

        count = 0
        i = 1
        while(count != k):
            
            if(i not in num_dict):
                count += 1
            
            i += 1

        return i - 1
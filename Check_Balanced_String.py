class Solution:
    def isBalanced(self, num: str) -> bool:
        
        even_indices_sum = odd_indices_sum = 0

        for i, e in enumerate(num):

            if(i % 2 == 0):
                even_indices_sum += int(e)
            else:
                odd_indices_sum += int(e)

        if(even_indices_sum == odd_indices_sum):
            return True
        else:
            return False
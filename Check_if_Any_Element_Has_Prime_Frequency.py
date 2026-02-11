from collections import Counter

class Solution:

    def is_prime(self, n):

        if(n == 1):
            return False

        elif(n == 2):
            return True

        i = 2
        root_n = n ** 0.5
        while(i <= root_n):

            if(n % i == 0):
                return False

            i += 1
        
        return True

    def checkPrimeFrequency(self, nums: list[int]) -> bool:
        
        freq_dict = Counter(nums)
        
        for freq in freq_dict.values():
            if(self.is_prime(freq)):
                return True
        

        return False
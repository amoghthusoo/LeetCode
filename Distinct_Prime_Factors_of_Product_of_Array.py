class Solution:
    def get_prime(self):

        i = 2
        while(True):
            
            j = 2
            while(j <= i ** 0.5):

                if(i % j == 0):
                    break
                j += 1  
            else:
                yield i

            i += 1

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        intr_set = set()

        gen = self.get_prime()
        primes = []
        while(True):
            p = next(gen)
            if(p <= 503):
                primes.append(p)
            else:
                break

        for num in nums:
            is_prime = True
            i = 0
            while(primes[i] <= num//2):
                if(num % primes[i] == 0):
                    intr_set.add(primes[i])
                    is_prime = False
                i += 1
            
            if(is_prime):
                intr_set.add(num)
        
        return len(intr_set)
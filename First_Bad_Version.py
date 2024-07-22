# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        lower_bound = 1
        upper_bound = n

        while(True):

            mid = (lower_bound + upper_bound) // 2

            is_bad = isBadVersion(mid)

            if(is_bad and mid == 1):
                return 1
            
            elif(is_bad and not isBadVersion(mid - 1)):
                return mid
            
            else:

                if(is_bad):
                    upper_bound = mid - 1
                else:
                    lower_bound = mid + 1

class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        
        lower_limit = int(event1[0][0:2] + event1[0][3:])
        upper_limit = int(event1[1][0:2] + event1[1][3:])

        if(upper_limit >= lower_limit):
            range1 = list(range(lower_limit, upper_limit + 1))

        else:
            range1 = list(range(lower_limit, 2360)) + list(range(0, upper_limit + 1))
        
        lower_limit = int(event2[0][0:2] + event2[0][3:])
        upper_limit = int(event2[1][0:2] + event2[1][3:])

        if(upper_limit >= lower_limit):
            range2 = list(range(lower_limit, upper_limit + 1))

        else:
            range2 = list(range(lower_limit, 2360)) + list(range(0, upper_limit + 1))

        

        if(len(list(set(range1) & set(range2))) != 0):
            return True
        else:
            return False


event1 = ["22:15","20:00"]
event2 = ["21:00","22:00"]
obj = Solution()
out = obj.haveConflict(event1, event2)
print(out)        
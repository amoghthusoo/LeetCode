from itertools import permutations
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        
        base_str = "0" * (10 - turnedOn) + "1" * turnedOn
        perms = permutations(base_str)
        unique_perms = set()
        for perm in perms:
            unique_perms.add(perm)
        
        ans = []
        for perm in unique_perms:
            hours = int("".join(perm[0 : 4]), 2)
            minutes = int("".join(perm[4 : ]), 2)

            if(hours <= 11 and minutes <= 59):
                hours = str(hours)
                minutes = str(minutes).zfill(2)
                ans.append(f"{hours}:{minutes}")
        
        return ans


turnedOn = 1
obj = Solution()
result = obj.readBinaryWatch(turnedOn)
print(result)
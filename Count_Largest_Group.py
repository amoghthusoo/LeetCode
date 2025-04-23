class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        group_dict = {}

        for i in range(1, n + 1):
            digit_sum = sum([int(j) for j in list(str(i))])
            if(digit_sum not in group_dict):
                group_dict[digit_sum] = 1
            else:
                group_dict[digit_sum] += 1
        
        _max = max(group_dict.values())

        count = 0
        for key, value in group_dict.items():
            if(value == _max):
                count += 1
    
        return count
    
n = 13
obj = Solution()
out = obj.countLargestGroup(n)
print(out)
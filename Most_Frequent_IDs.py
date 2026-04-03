from sortedcontainers import SortedDict
class Solution:
    def mostFrequentIDs(self, nums: list[int], freq: list[int]) -> list[int]:
        
        d = dict()
        rd = SortedDict()
        ans = []

        for i in range(len(nums)):

            num = nums[i]
            f = freq[i]

            if(num not in d):
                d[num] = f
            
                if(f not in rd):
                    rd[f] = {num}
                else:
                    rd[f].add(num)

            else:

                future_val = d[num] + f
                rd[d[num]].remove(num)

                if(len(rd[d[num]]) == 0):
                    rd.pop(d[num])

                if(future_val == 0):
                    d.pop(num)
                
                else:
                    d[num] = future_val

                    if(future_val not in rd):
                        rd[future_val] = {num}
                    else:
                        rd[future_val].add(num)
            
            try:
                k, v = rd.peekitem(-1)
                ans.append(k)
            except:
                ans.append(0)
        
        return ans

nums = [7,7]
freq = [3,5]
obj = Solution()
result = obj.mostFrequentIDs(nums, freq)
print(result)
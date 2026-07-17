class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        
        intr_dict = dict()
        running_set = dict()

        for i in range(k):
            running_set[nums[i]] = running_set.get(nums[i], 0) + 1
        
        i = 0
        j = k - 1
        while(j < len(nums)):

            for e in running_set:
                intr_dict[e] = intr_dict.get(e, 0) + 1
            
            running_set[nums[i]] -= 1
            if(running_set[nums[i]] == 0):
                running_set.pop(nums[i])
            i += 1

            j += 1
            try:
                running_set[nums[j]] = running_set.get(nums[j], 0) + 1
            except:
                pass
        
        poss_ans = []
        for num, occr in intr_dict.items():
            if(occr == 1):
                poss_ans.append(num)
        
        try:
            return max(poss_ans)
        except:
            return -1
            
        
nums = [3,9,2,1,7]
k = 3
obj = Solution()
result = obj.largestInteger(nums, k)
print(result)
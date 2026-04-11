class Solution:
    def minimumDistance(self, nums: list[int]) -> int:

        def get_min_dis(arr):

            res = float("inf")

            i = 0
            while(i < len(arr) - 2):

                res = min(res, abs(arr[i] - arr[i + 1]) + abs(arr[i + 1] - arr[i + 2]) + abs(arr[i] - arr[i + 2]))
                i += 1

            return res
        
        idx_dict = dict()

        for i, num in enumerate(nums):

            if(num not in idx_dict):
                idx_dict[num] = [i]
            else:
                idx_dict[num].append(i)


        res = float("inf")
        for num, indices in idx_dict.items():

            if(len(indices) >= 3):
                pos_res = get_min_dis(indices)

                res = min(res, pos_res)
        
    
        return res if res != float("inf") else -1
    

nums = [1]
obj = Solution()
result = obj.minimumDistance(nums)
print(result)
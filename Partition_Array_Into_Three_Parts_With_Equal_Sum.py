class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:

        total = sum(arr)

        if(total/3 != total//3):
            return False

        intr_ans = 0
        part = total // 3       
        cm_sum = 0
        for num in arr:
            cm_sum += num
            if(cm_sum == part):
                cm_sum = 0
                intr_ans += 1

        if(intr_ans >= 3):
            return True
        else:
            return False
        
arr = [1,-1,1,-1]
obj = Solution()
result = obj.canThreePartsEqualSum(arr)
print(result)
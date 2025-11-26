class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        
        ans = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):

                if(abs(arr1[i] - arr2[j]) <= d):
                    break
            
            else:
                ans += 1
            
        return ans

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
obj = Solution()
result = obj.findTheDistanceValue(arr1, arr2, d)
print(result)

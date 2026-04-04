class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        
        threshold *= k

        ans = 0

        total = 0
        j = 0
        while(j < k):
            total += arr[j]
            j += 1
        
        j -= 1
        if(total >= threshold):
            ans += 1

        i = 0

        while(j < len(arr) - 1):
            
            total -= arr[i]
            i += 1
            
            j += 1
            total += arr[j]

            if(total >= threshold):
                ans += 1
            
        return ans 

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
obj = Solution()
result = obj.numOfSubarrays(arr, k, threshold)
print(result)
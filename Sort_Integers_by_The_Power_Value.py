class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        dp = dict()

        for i in range(lo, hi + 1):

            temp = [i]
            cnt = 0
            while(i != 1):

                if(i not in dp):

                    if(i % 2 == 0):
                        i //= 2
                    else:
                        i = i * 3 + 1
                    
                    temp.append(i)
                    cnt += 1
                
                else:
                    cnt += dp[i]
                    break
            
            j = 0
            while(j < len(temp)):
                dp[temp[j]] = cnt
                cnt -= 1
                j += 1

        intr_arr = []
        for i in range(lo, hi + 1):
            intr_arr.append((dp[i], i))
        intr_arr.sort()
        return intr_arr[k - 1][1]

lo = 10
hi = 15
k = 2
obj = Solution()
result = obj.getKth(lo, hi, k)
print(result)
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        intr_arr = []

        one_mem = True
        i = len(s) - 1
        while(i >= 0):
            
            if(s[i] == "0"):
                i
                intr_arr.insert(0, s[i])

            else:
                if(one_mem):
                    
                    if(int("1" + "".join(intr_arr), 2) <= k):
                        intr_arr.insert(0, s[i])
                    else:
                        one_mem = False

            i -= 1

        return len(intr_arr)

s = "00101001"
k = 1
obj = Solution()
result = obj.longestSubsequence(s, k)
print(result)
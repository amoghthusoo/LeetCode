class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        
        out_arr = []
        out_arr.append(pref[0])

        i = 1
        while(i < len(pref)):
            
            out_arr.append(pref[i] ^ pref[i - 1])
            
            i += 1

        return out_arr
    
pref = [5,2,0,3,1]
obj = Solution()
out = obj.findArray(pref)
print(out)
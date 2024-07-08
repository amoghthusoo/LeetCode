class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        
        for e in arr:

            if(e == 0 and (arr.count(0) >= 2)):
                return True
            
            elif(e * 2 in arr and e != 0):
                return True
            

        return False
    
arr = [-2,0,10,-19,4,6,-8]
obj = Solution()
out = obj.checkIfExist(arr)
print(out)
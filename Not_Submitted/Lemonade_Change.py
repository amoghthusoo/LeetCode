class Solution:
    
    def lemonadeChange(self, bills: list[int]) -> bool:
        
        change_dict = {
            5 : 0,
            10 : 0,
            20 : 0
        }

        for bill in bills:
            
            if(bill == 5):
                change_dict[5] += 1

            elif(bill == 10):

                if(change_dict[5] != 0):
                    
                    change_dict[10] += 1
                    change_dict[5] -= 1
                
                else:
                    return False
            
            elif(bill == 20):

                if(change_dict[5] != 0 and change_dict[10] != 0):
                    
                    change_dict[20] += 1
                    change_dict[5] -= 1
                    change_dict[10] -= 1

                elif(change_dict[5] >= 3):

                    change_dict[20] += 1
                    change_dict[5] -= 3

                else:
                    return False
            
        return True
    
bills = [5,5,10,10,20]
obj = Solution()
out = obj.lemonadeChange(bills)
print(out)
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    nums = list(logs["num"])

    if(len(nums) == 0):
        return pd.DataFrame([], columns=["ConsecutiveNums"])
    
    cons_nums = set()

    current = nums[0]
    count = 1
    i = 1
    while(i < len(nums)):

        if(nums[i] == current):
            count += 1
        
        else:

            if(count >= 3):
                cons_nums.add(current)
            
            count = 1
            current = nums[i]
        
        i += 1

    if(count >= 3):
        cons_nums.add(current)
    

    return pd.DataFrame(list(cons_nums), columns = ["ConsecutiveNums"])
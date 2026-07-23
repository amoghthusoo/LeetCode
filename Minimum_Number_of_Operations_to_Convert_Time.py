class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        current_hours = int(current[0 : 2])
        current_minutes = int(current[3 : ])
        
        correct_hours = int(correct[0 : 2])
        correct_minutes = int(correct[3 : ])

        total_minutes = (correct_hours - current_hours) * 60 + (correct_minutes - current_minutes)

        steps = 0
        while(total_minutes > 0):

            if(total_minutes - 60 >= 0):
                total_minutes -= 60
                steps += 1
            
            elif(total_minutes - 15 >= 0):
                total_minutes -= 15
                steps += 1

            elif(total_minutes - 5 >= 0):
                total_minutes -= 5
                steps += 1
            
            else:
                total_minutes -= 1
                steps += 1
        
        return steps

current = "02:30"
correct = "04:35"
obj = Solution()
result = obj.convertTime(current, correct)
print(result)
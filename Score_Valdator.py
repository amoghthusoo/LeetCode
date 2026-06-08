class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        
        score, counter = 0, 0
        i = 0
        while(i < len(events) and counter < 10):
            
            if(events[i] not in {"W", "WD", "NB"}):
                score += int(events[i])
            
            elif(events[i] == "W"):
                counter += 1
            
            else:
                score += 1

            i += 1
        
        return [score, counter]

events = ["1","4","W","6","WD"]
obj = Solution()
result = obj.scoreValidator(events)
print(result)
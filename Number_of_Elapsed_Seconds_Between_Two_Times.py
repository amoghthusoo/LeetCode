class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        
        start_hours = int(startTime[0 : 2])
        start_minutes = int(startTime[3 : 5])
        start_secs = int(startTime[6 : 8])
        
        end_hours = int(endTime[0 : 2])
        end_minutes = int(endTime[3 : 5])
        end_secs = int(endTime[6 : 8])

        return (end_secs - start_secs) + (end_minutes - start_minutes) * 60 + (end_hours - start_hours) * 3600



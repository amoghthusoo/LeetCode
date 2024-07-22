class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:

        time_difference = []
        time_difference.append(releaseTimes[0])

        i = 1
        while(i < len(releaseTimes)):
            
            time_difference.append(releaseTimes[i] - releaseTimes[i - 1])
            
            i += 1

        max_duration = max(time_difference)

        max_char = 96

        i = 0
        while(i < len(time_difference)):
            
            if(time_difference[i] == max_duration):
                if(ord(keysPressed[i]) > max_char):
                    max_char = ord(keysPressed[i])
            i += 1

        return chr(max_char)
    
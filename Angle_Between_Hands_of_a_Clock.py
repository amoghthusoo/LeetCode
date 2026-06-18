class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hour_map = dict()

        for i in range(1, 13):
            hour_map[i] = (i * 30) % 360

        minute_angle = minutes * 6
        hour_angle = hour_map[hour] + minute_angle / 12

        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)

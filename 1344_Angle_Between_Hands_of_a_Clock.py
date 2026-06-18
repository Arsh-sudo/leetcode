class Solution:
    def angleClock(self, hour, minutes):
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        minute_angle = minutes * 6

        diff = abs(hour_angle - minute_angle)

        return min(diff, 360 - diff)
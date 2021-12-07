

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # find the minute degree
        # find the hour degree
        # minutes
        # how many minutes in a clock cycle = 60 minutes/ 1hr
        # 1 cycle is 360 degrees
        # so for 1 minute is 360/60 so 6 degrees per minute
        # Hour
        # 12 hrs = 360 deg
        # 1 hr is 360/12 => 30 deg per hour
        # but then it depends on the minute
        # so we need to analyze the minute as well
        # let say 1:30, 
        # 12 hrs is 360 deg, between 1:00 and 2:00 we have 30deg, so we split depending on each minute, 30/60 => 0.5
        # let say 1:30, 
        
        
        hour_angle = 30 * hour + 0.5 * minutes
        minute_angle = 6 * minutes
        
        diff1 = abs(hour_angle - minute_angle)
        diff2 = 360 - diff1
        
        return min(diff1, diff2)
        
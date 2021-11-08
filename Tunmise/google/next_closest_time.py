class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        h, m = time.split(":")
        curr = int(h) * 60 + int(m) #get time in mins
        result = None
        for i in range(curr+1, curr+1441):
            t = i % 1440 #mod by 1440 to get 00:00 after 23:59
            h, m = t // 60, t % 60
            result = "%02d:%02d" % (h, m)
            if set(result) <= set(time):
                break
        return result
class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.n = 0
        self.s = size
        self.total = 0
        self.arr = []
        self.i = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        self.arr.append(val)
        self.total += val
        self.n += 1
        if self.n > self.s:
            self.total -= self.arr[self.i]
            self.i += 1
            self.n = self.s
        return self.total/self.n
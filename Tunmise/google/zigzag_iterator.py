class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        #create a zigzag list and a next pointer
        self.z = []
        self.next_i = -1
        i,j = 0,0
        while i < len(v1) or j < len(v2):
            if i < len(v1):
                self.z.append(v1[i])
                i += 1
            if j < len(v2):
                self.z.append(v2[j])
                j += 1


    """
    @return: An integer
    """
    def _next(self):
        # write your code here
        return self.z[self.next_i]
         

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        if self.next_i + 1 < len(self.z):
            self.next_i += 1
            return True
        else:
            return False
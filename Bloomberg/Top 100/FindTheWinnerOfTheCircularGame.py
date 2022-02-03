


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ## n = 6 , k = 5
        ## [1,2,3,4,5,6] , remove 5. arr becomes [1,2,3,4,6]
        ## since we are counting from 6 and wrap around the array
        ## we can just put the reset of the array starting from '6' to the beginning,
        ## e.g [1,2,3,4,6] => [6,1,2,3,4]
        ## this way it would be easier to find the kth index. 
        ## if ind == -1 : => we need to remove the last element,
        ## else : do the above operation
        
        arr = [i+1 for i in range(n)]
        
        while len(arr) > 1:
            ind =   k  %  len(arr) -1
            if ind == -1:
                arr = arr[:-1]
            else:
                arr =   arr[ind+1:] + arr[:ind]
                
        return arr[0]
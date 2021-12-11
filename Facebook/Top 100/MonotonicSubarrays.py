

def countIncreasing(arr, n):
     
    # Initialize count of subarrays as 0
    cnt = 0
 
    # Pick starting point
    for i in range(0, n) :
         
        # Pick ending point
        for j in range(i + 1, n) :
            if arr[j] > arr[j - 1] :
                cnt += 1
 
            # If subarray arr[i..j] is not strictly
            # increasing, then subarrays after it , i.e.,
            # arr[i..j+1], arr[i..j+2], .... cannot
            # be strictly increasing
            else:
                break

                # Pick ending point
        for j in range(i + 1, n) :
            if arr[j] < arr[j - 1] :
                print(arr[j],arr[j - 1] )
                cnt += 1
 
            # If subarray arr[i..j] is not strictly
            # increasing, then subarrays after it , i.e.,
            # arr[i..j+1], arr[i..j+2], .... cannot
            # be strictly increasing
            else:
                break
    return cnt


print(countIncreasing([1,2,3,4,3,1], 6))
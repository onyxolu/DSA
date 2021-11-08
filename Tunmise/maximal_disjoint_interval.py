# Python3 implementation of the approach

# Function to find maximal disjoint set 
def maxDisjointIntervals(list_):
	
	# Lambda function to sort the list 
	# elements by second element of pairs 
	list_.sort(key = lambda x: x[1])
	
	# First interval will always be 
	# included in set 
	print("[", list_[0][0], ", ", list_[0][1], "]")
	
	# End point of first interval
	r1 = list_[0][1]
	
	for i in range(1, len(list_)):
		l1 = list_[i][0]
		r2 = list_[i][1]
		
		# Check if given interval overlap with 
		# previously included interval, if not 
		# then include this interval and update 
		# the end point of last added interval
		if l1 > r1:
			print("[", l1, ", ", r2, "]")
			r1 = r2
			

# Driver code 
if __name__ == "__main__":
	
	N = 4
	intervals = [ [ 1, 5 ], [ 2, 7],
				[ 11, 18 ] ]
	
	# Call the function
	maxDisjointIntervals(intervals)

# This code is contributed by Tokir Manva

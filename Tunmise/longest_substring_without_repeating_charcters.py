def longestSubstringWithoutDuplication(string):
    # Write your code here.


	start = 0
	longest = [0,1]
	lastSeen = {}
	for i ,char in enumerate(string):
		if char in lastSeen:
			start = max(start,lastSeen[char] +1)
		if longest[1] - longest[0] < i - start +1:
			longest[0],longest[1] = start, i+1
		lastSeen[char] = i
	return string[longest[0]:longest[1]]
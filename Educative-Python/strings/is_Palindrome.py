def palindrome(str):
    clean_str = ''
    for val in str:
        if val.isalnum():
            clean_str += val.lower()
    print(clean_str)
    return clean_str == clean_str[::-1]

    # s = re.sub('[^0-9a-zA-Z]', '', s.lower())

	# if s != s[::-1]:
	# 	return False
	# return True

print(palindrome("radar??"))


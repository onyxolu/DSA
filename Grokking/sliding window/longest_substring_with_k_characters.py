str = "cbbebi"



# // window_start, window_end, window_value = dic(), max_length
# // loop through string
# // add up strings to hashmap with key = (strval) , value = no of occurrence
# // do a check for k distinct characters using the hashmap
# // if true get max length, then I slide the window_end
# // if not shrink the window



def longestSubstring(str, k):
    dict = {}
    maxStr = ""
    windowValue = "" 
    for windowKey in range(len(str)):
        currentStr = str[windowKey]
        windowValue += currentStr
        if(currentStr in dict):
            dict[currentStr] += 1
        else: 
            dict[currentStr] = 1

        if len(dict) > k:
            firstLetter = windowValue[0]
            if dict[firstLetter] > 1:
                dict[firstLetter] -= 1
            else:
                del dict[firstLetter]
            windowValue = windowValue[1:]
        else: 
            if len(windowValue) > len(maxStr):
                maxStr = windowValue
       

    return maxStr


print(longestSubstring(str, 3))







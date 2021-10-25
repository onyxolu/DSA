import math

str = "araaci" 
k = 2
# expected output = 2

# pattern => sliding window
# create a dict for str freq 
# when dict length exceeds k, shrink
# remove left elem from dict 
# keep track of maxlength
# return maxlength

def longSubstr(str, k):
    freq = {}
    w_start = 0
    max_len = -math.inf
    for w_end in range(len(str)):
        cur_str = str[w_end]
        if cur_str in freq:
            freq[cur_str] += 1
        else:
            freq[cur_str] = 1
        while len(freq) >= k:
            left_val = str[w_start]
            max_len = max(max_len, w_end - w_start +1)
            # print(freq, left_val)
            if left_val in freq:
                freq[left_val] -= 1
            if freq[left_val] == 0:
                del freq[left_val]
            w_start += 1
    return max_len

print(longSubstr(str, k))

            
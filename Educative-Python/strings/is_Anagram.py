def anagram(s1, s2):
    clean_str1 = ''
    clean_str2 = ''
    for val in s1:
        if val.isalnum():
            clean_str1 += val.lower()
    for val in s2:
        if val.isalnum():
            clean_str2 += val.lower()
    print(clean_str1, clean_str2)
    return sorted(clean_str1) == sorted(clean_str2)

print(anagram("William Shakespeare", "I am a weakish speller"))

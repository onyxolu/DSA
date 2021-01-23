
str = "catfoxcat" 
Words = ["cat", "fox"]

# check for empty Word and return []
# create a dic for word_frequency
# loop the string till word.length * word[0] length
# create a dic for word_seen and check for the words

def word_concat(str, words):
    result_indices = []
    word_frequency = {}

    if len(words) == 0 or len(words[0]) == 0:
        return []

    words_length = len(words)
    word_length = len(words[0])

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    for i in range((len(str) - word_length * words_length) + 1):
        word_seen = {}
        for j in range(words_length):
            print("j", j)
            word_idx = i + j * word_length 
            word = str[word_idx: word_idx + word_length]

            if word not in word_frequency:
                break

            if word not in word_seen:
                word_seen[word] = 0
            word_seen[word] += 1
            print(word)

            if word_seen[word] > word_frequency.get(word, 0):
                break


            if j + 1 == words_length:
                print(j)
                result_indices.append(i)

    return result_indices

print(word_concat(str, Words))




    




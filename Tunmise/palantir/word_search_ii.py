def find_embedded_word(words,string):
    from collections import defaultdict
    from copy import deepcopy
    d = defaultdict(int)
    res =[]
    for char in string:
        d[char] += 1

    for s in words:
        temp = deepcopy(d)
        flag = True
        for c in s:
            if temp[c] <= 0:
                flag = False
                break
            temp[c] -= 1
        
        if flag:
            res.append(s)
    if len(res) == 0:
        res.append("None")
    print(res)

words = ['cat', 'cab', 'dog', 'bird', 'car', 'ax']
string1 = 'tcabnihjs'
find_embedded_word(words, string1) #cat

string2 = 'tbcanihjs'
find_embedded_word(words, string2) #cat

string3 = 'baykkjl'
find_embedded_word(words, string3) #None

string4 = 'bbabylkkj'
find_embedded_word(words, string4) #baby

string5 = 'ccc'
find_embedded_word(words, string5) #None

string6 = 'nbird'
find_embedded_word(words, string6) #bird


# def find_word_location( board, word):
#         path = []
        
#         def find(board,word,row,col,i, path_so_far):
#             if i == len(word):
#                 path.append(path_so_far[:-1])
#                 return True
#             if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[i]:
#                 return False

#             board[row][col] = "#"
#             res = find(board,word,row,col+1,i+1, path_so_far + [(row, col+1)]) or find(board,word,row,col-1,i+1, path_so_far + [(row, col-1)]) or find(board,word,row+1,col,i+1, path_so_far + [(row+1, col)]) or find(board,word,row-1,col,i+1, path_so_far + [(row-1, col)])
#             board[row][col] = word[i]

#             return res
        
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     if find(board,word,i,j, 0, [(i, j)]):
#                         print(path[0])
#                         return
#         return []
        
# grid1 = [
# 	['c', 'c', 'c', 'a', 'r', 's'],
# 	['c', 'c', 'i', 't', 'n', 'b'],
# 	['a', 'c', 'n', 'n', 't', 'i'],
# 	['t', 'c', 'i', 'i', 'p', 't']
# ]

# word1_1 = "catnip"
# find_word_location(grid1, word1_1)# [ (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4) ]

# word1_2 = "cccc"
# find_word_location(grid1, word1_2)# [(0, 1), (1, 1), (2, 1), (3, 1)]
# # OR [(0, 0), (1, 0), (1, 1), (2, 1)]
# # OR [(0, 0), (0, 1), (1, 1), (2, 1)]
# # OR [(1, 0), (1, 1), (2, 1), (3, 1)]


# grid2 = [
#     ['c', 'p', 'a', 'n', 't', 's'],
#     ['a', 'b', 'i', 't', 'a', 'b'],
#     ['t', 'f', 'n', 'n', 'c', 'i'],
#     ['x', 's', 'c', 'a', 't', 'n'],
#     ['x', 's', 'd', 'd', 'e', 'a'],
#     ['s', 'q', 'w', 'x', 's', 'p']
# ]


# word2 = "catnap"
# find_word_location(grid2, word2)# [ (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5) ]

# grid3 = [
#     ['c', 'r', 'c', 'a', 'r', 's'],
#     ['a', 'b', 'i', 't', 'n', 'i'],
#     ['t', 'f', 'n', 'n', 'x', 'p'],
#     ['x', 's', 'i', 'x', 'p', 't']
# ]
# word3 = "catnip"
# find_word_location(grid3, word3)# [ (0, 2), (0, 3), (1, 3), (1, 4), (1, 5), (2, 5) ]

# grid4 = [
#     ['a', 'o', 'o', 'o', 'a', 'a'],
#     ['b', 'b', 'i', 't', 'n', 'i'],
#     ['c', 'f', 'n', 'n', 'v', 'p'],
#     ['o', 'a', 'a', 'a', 'o', 'o']
# ]
# word4_1 = "aaa"
# word4_2 = "ooo"

# find_word_location(grid4, word4_1)# [ (3, 1), (3, 2), (3, 3) ]
# find_word_location(grid4, word4_2)#[ (0, 1), (0, 2), (0, 3) ]
                
            
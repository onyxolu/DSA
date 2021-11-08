from itertools import combinations
def count_teams(skills,minl,maxl,minAss):
    l = []
    for ele in skills:
        if ele>=minl and ele<=maxl:
            l.append(ele)
    num_of_teams = 0
    while minAss <= len(l):
        comb =len(list(combinations(l,minAss)))
        num_of_teams += comb
        minAss += 1
    return num_of_teams
print(count_teams([12, 4, 6, 13, 5, 10],4,10,3))
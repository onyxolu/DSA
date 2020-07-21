
tlist = [
"Anne", 100, 1, "Boston",
"Anne", 2000, 10, "Boston",
"Bob", 50, 20, "Boston",
"Cindy", 100, 50, "New York",
"Bob", 50, 70, "New York" ]

trans = {}

fraud = []

def calc():
  for i,v in enumerate(tlist[::4]):
    firstIdx = i * 4
    name = tlist[firstIdx]
    transItem = [ tlist[firstIdx], tlist[firstIdx+1], tlist[firstIdx+2], tlist[firstIdx+3]]

    if(transItem[1] > 1000):
      fraud.append(transItem)

    if name in trans:
      old = trans[name]
      if old[3] != transItem[3] and transItem[2] - old[2] < 60:
        fraud.append(old)
        fraud.append(transItem) 

    trans[name] = transItem

  print(fraud) 

        
calc()
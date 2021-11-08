from collections import defaultdict
def get_mid(pre_req):
    
    adj = defaultdict(list)
    in_deg, out_deg = set(), set()
    
    for a, b in pre_req:
        adj[a].append(b)
        in_deg.add(b)
        out_deg.add(a)
        
    n, source = len(pre_req), (out_deg - in_deg).pop()
    for _ in range(n//2):
        source = adj[source][0]
    return source


prereqs_courses1 = [
      ["Foundations of Computer Science", "Operating Systems"],
      ["Data Structures", "Algorithms"],
      ["Computer Networks", "Computer Architecture"],
      ["Algorithms", "Foundations of Computer Science"],
      ["Computer Architecture", "Data Structures"],
      ["Software Design", "Computer Networks"]
  ] 
prereqs_courses2 = [
      ["Data Structures", "Algorithms"],
      ["Algorithms", "Foundations of Computer Science"],
      ["Foundations of Computer Science", "Logic"]
  ]
prereqs_courses3 = [
      ["Data Structures", "Algorithms"],
  ]

print(get_mid(prereqs_courses1))
print(get_mid(prereqs_courses2))
print(get_mid(prereqs_courses3))
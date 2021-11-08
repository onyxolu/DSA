def get_activity(badge_times):
    import collections
    ptod = collections.defaultdict(list)
    ls = {}
    for i in badge_times:
        ptod[i[0]].append(i[1])

    for person,times in ptod.items():
        # print (k,v)
        window_times = set()
        if len(times) >= 3:
            times = sorted([int(x) for x in times])
        for i in range(0, len(times)):
            j = i+1
            while j < len(times):
                if times[j] - times[i] <= 100:
                    window_times.add(times[j])
                    window_times.add(times[i])
                elif len(window_times) > 2 :
                    ls[person] = window_times
                    break
                j+=1
            if person in ls:
                break
            elif len(window_times) > 2:
                ls[person] = window_times
            
    for person,times in ls.items():
        if len(times) > 0:
            times = sorted([int(x) for x in times])
            print (person,times)
def security_check(access_list):
    return_result = dict()
    access_data_dict = dict()
    for employee in access_list:
        if employee[0] not in access_data_dict:
            access_data_dict[employee[0]] = [employee[1]]
        else:
            access_data_dict[employee[0]].append(employee[1])

    for name, val in access_data_dict.items():
        if len(val) >= 3:
            val = sorted([int(p) for p in val]) #this sort takes O(nlogn) and I changed the value type to int so I get it in the right order.
            start = 0
            start_time = val[start]
            time_result = [start_time]
            for x in range(start + 1, len(val)):
                if val[x] - start_time <= 100:
                    time_result.append(val[x])
                    if len(time_result) >= 3:
                        if name not in return_result:
                            return_result[name] = time_result
                else:
                    start += 1
                    start_time = val[start]
                    time_result = [start_time]

    return return_result
badge_times = [
  ["Paul",     "1355"],
  ["Jennifer", "1910"],
  ["John",      "835"],
  ["John",      "830"],
  ["Paul",     "1315"],
  ["John",     "1615"],
  ["John",     "1640"],
  ["Paul",     "1405"],
  ["John",      "855"],
  ["John",      "930"],
  ["John",      "915"],
  ["John",      "730"],
  ["John",      "940"],
  ["Jennifer", "1335"],
  ["Jennifer",  "730"],
  ["John",     "1630"],
  ["Jennifer",    "5"]
]
print(security_check(badge_times))
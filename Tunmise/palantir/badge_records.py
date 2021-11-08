def check_badges(badges_list):
    processed_data = dict()
    employee_list_in = []
    employee_list_out = []
    for input_data in badges_list:
        if input_data[0] not in processed_data:
            processed_data[input_data[0]] = [input_data[1]]
        else:
            processed_data[input_data[0]].append(input_data[1])

    #     check if either 'enter' or 'exit' in sequence in the list.
    for key, value in processed_data.items():
        for index in range(len(value) - 1):
            if (value[index] == 'enter') and (value[index + 1] == 'enter'):
                if key not in employee_list_in:
                    employee_list_in.append(key)
            if (value[index] == 'exit') and (value[index + 1] == 'exit'):
                if key not in employee_list_out:
                    employee_list_out.append(key)
    print(f"{employee_list_in}, {employee_list_out}")
badge_records = [
  ["Paul" ,  "enter"],
  ["Paul" ,  "enter"],
  ["Curtis" , "enter"],
  ["Paul" , "exit"],
  ["John" , "exit"],
  ["Paul" , "exit"],
  ["Jennifer" , "exit"],
  ["Curtis" , "exit"],
  ["John" , "enter"],
  ["Jennifer" , "enter"],
  ["Curtis" ,  "enter"],
  ["John" , "enter"],
  ["Jennifer" , "enter"],
  ["John" , "exit"],
  ["Curtis" , "exit"],
  ["Jennifer" , "exit"],
]

badge_records_1 = [
["Martha", "exit"],
["Paul", "enter"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "enter"],
["Paul", "enter"],
["Curtis", "exit"],
["Curtis", "enter"],
["Paul", "exit"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "exit"],
["Paul", "enter"],
["Paul", "enter"],
["Martha", "exit"],
]


print(check_badges(badge_records_1))
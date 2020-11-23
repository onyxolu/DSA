def is_unique(input_str):
  seen = []
  for val in input_str:
    if val in seen:
      return False
    else:
      seen.append(val)
  return True

# def is_unique_2(input_str):
#     return len(set(input_str)) == len(input_str)


print(is_unique("olumide"))
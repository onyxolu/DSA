def decode_string(s):
    k = 0
    stack = []
    output = ""

    for char in s:
        if char.isdigit():
            k = k*10 + int(char)
        elif char == "[":
            stack.append([output,k])
            output = ""
            k = 0
        elif char == "]":
            prev_output,prev_k =stack.pop()
            output = prev_output + prev_k*output
        else:
            output += char
    return output
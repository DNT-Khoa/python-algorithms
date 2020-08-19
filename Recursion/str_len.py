# Given a string, calculate the length of the string

input_str = "LucidProgramming"

def iterative_str_len(input_str):
    length = 0

    for _ in range(len(input_str)):
        length += 1
    
    return length


def recursion_str_len(input_str):
    if input_str == '':
        return 0
    
    return 1 + recursion_str_len(input_str[1:])


print(recursion_str_len(input_str))
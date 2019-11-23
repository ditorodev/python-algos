def reverse_string(str):
    if len(str) == 1:
        return str[len(str)-1];
    

    return str[len(str)-1] + reverse_string(str[0:(len(str) - 1)])


print(reverse_string('hello'))
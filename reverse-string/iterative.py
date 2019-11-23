def reverse_string(str):
    newStr = ''

    for i in range(1, len(str)+1):
        newStr = newStr + str[len(str) - i];

    return newStr;

print(reverse_string('hello'))
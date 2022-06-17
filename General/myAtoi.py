def myAtoi(s):
    s = s.strip().split()[0]
    lower_limit = -2**31
    upper_limit = 2**31 - 1
    sign = True
    new_num = ''
    if s.isdigit() or s[0] == '+':
        if s[1].isdigit():
            print('+', int(s))
    elif s.isdigit() and s[0] == '-':
        if s[1].isdigit():
            print('-', s)
    flag = 0
    for ele in s:
        if ele == '+' or ele == '-' or ele.isdigit():
            if ele == '0':
                continue
            elif ele == '-' and flag <= 2:
                flag += 1
                if flag == 2:
                    return 0
                sign = False
            elif ele == '+' and flag <= 2:
                flag += 1
                if flag == 2:
                    return 0

    


print(myAtoi('12'))
print(myAtoi('+12'))
print(myAtoi('-12'))
print(myAtoi('+-12'))
print(myAtoi("00000-42a1234"))
print(myAtoi("00000-42a1234 saff"))
print(myAtoi("safs 00000-42a1234"))

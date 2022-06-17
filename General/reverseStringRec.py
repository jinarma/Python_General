def rev(string, l1):
    if bool(string) == False:
        return ''.join(l1)
    else:
        l1.append(string[-1])
        return rev(string[:-1], l1)
s1 = input()
l1 = []
print('The reversed string is:', rev(s1, l1))
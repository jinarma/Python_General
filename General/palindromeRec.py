def palindrome(string, n1, n2, count):
    if count == len(string):
        return 'true'
    elif count > len(string):
        return 'false'
    else:
        if string[n1] == string[n2]:
            count += 1
            n1 += 1
            n2 -= 1
            return palindrome(string, n1, n2, count)
        else:
            count = len(string)+10
            return palindrome(string, n1, n2, count)


ls1 = input()
print(palindrome(ls1, 0, len(ls1)-1, 0))
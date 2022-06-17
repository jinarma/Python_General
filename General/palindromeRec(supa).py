def pallindrome(string):
    if len(string) == 0 or len(string) == 1:
        return "true"
    else:
        if string[0] != string[-1]:
            return "false"
        else:
            return pallindrome(string[1:-1])


string = "madam"
print(pallindrome(string))
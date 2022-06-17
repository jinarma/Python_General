if __name__ == '__main__':
    s = input()
    count = len(s)-1
    for i, ele in enumerate(s):
        if ele.isalnum():
            print('True')
            break
        if i == count:
            print('False')
    for i, ele in enumerate(s):
        if ele.isalpha():
            print('True')
            break
        if i == count:
            print('False')
    for i, ele in enumerate(s):
        if ele.isdigit():
            print('True')
            break
        if i == count:
            print('False')
    for i, ele in enumerate(s):
        if ele.islower():
            print('True')
            break
        if i == count:
            print('False')
    for i, ele in enumerate(s):
        if ele.isupper():
            print('True')
            break
        if i == count:
            print('False')
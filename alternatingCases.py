def check(password):
    for i, ele in enumerate(password):
        if i == len(password) - 1:
            return [True, len(password)]
        if ele.isupper() and password[i+1].isupper():
            return [False, i]
        elif ele.islower() and password[i+1].islower():
            return [False, i]


password = input()
result = check(password)
print(result[0], result[1], sep='\n')
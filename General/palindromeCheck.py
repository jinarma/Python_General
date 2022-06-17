# You are using Python
string = 'abb' #input()
start = 0 #int(input())
end = 3 #int(input())
string = string[start:end]
count = 0
for i in range(len(string)):
    for j in range(i+1, len(string)+1):
        temp = string[i:j]
        if temp == temp[::-1]:
            print(temp)
            count += 1
        else:
            continue

print(count)

# string = 'abc'
# print(string[0:3])
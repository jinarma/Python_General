size = int(input())
inc_list = list(map(int, input().split()))
char_list = list(input())
new_char_list = []
for i, ele in enumerate(char_list):
    while inc_list[i] > 25:
        inc_list[i] -= 26
    new_char_list.append(chr(ord(ele)+inc_list[i]))
string = ''.join(new_char_list)
print(string)
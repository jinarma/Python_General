""" 
# Fill replacement string on left and right side of string for a total size of width
string.center(width, replacement_string)

# Fill replacement string on left side of string for a total size of width
string.ljust(width, replacement_string)

# Fill replacement string on right side of string for a total size of width
string.rjust(width, replacement_string)

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
top_full = 2*num-1
left_space = (top_full-num)//2
mid_width = num*5
# cone (top right)
for i in range(num):
    print(('H'*(2*i+1)).center(top_full, ' '))

# mid columns (top)
for i in range(num+1):
    print(('H'*num).rjust(left_space+num, ' '), end='')
    print(' '*(num*3), end='')
    print('H'*num)
# mid section (mid)
for i in range(num//2+1):
    print(' '*left_space, end='')
    print('H'*num*5)

# mid columns (bottom)
for i in range(num+1):
    print(('H'*num).rjust(left_space+num, ' '), end='')
    print(' '*(num*3), end='')
    print('H'*num)

# cone (bottom left)
for i in range(num-1, -1, -1):
    print((' '*num).rjust(left_space+num, ' '), end='')
    print(' '*(num*4 + left_space - top_full), end='')
    print(('H'*(2*i+1)).center(top_full, ' '))

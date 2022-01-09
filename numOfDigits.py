def dig(count, num):
    if num == 0:
        return count
    else:
        count += 1
        return dig(count, num//10)
num = int(input())
print('The number of digits in {} is {}'.format(num, dig(0, num)))

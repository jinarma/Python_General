def sum_of_D(num):
    if num == 0:
        return 0
    else:
        temp = num % 10
        return sum_of_D(num//10)+temp


num = int(input())
print('The sum of digits in {} is {}'.format(num, sum_of_D(num)))

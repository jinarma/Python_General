def wordCount(list1):
    count = 0
    tempList = []
    sumList = []
    while list1:
        sum1 = 0
        if list1[0] in list1:
            temp = list1[0]
            count += 1
            for i in list1:
                if i != temp:
                    tempList.append(i)
                else:
                    list1.remove(i)
                    sum1 += 1
        sumList.append(str(sum1))
    print(count)
    temp_new = ' '.join(sumList)
    print(temp_new)

size = int(input())
wordList = []
for i in range(size):
    wordList.append(input())
wordCount(wordList)
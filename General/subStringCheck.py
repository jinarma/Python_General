# find all substrings of a string, starting with a consonant (duplicates are accepted and counted as many times as they occur)

def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    count_stuart = 0
    count_kevin = 0
    for i in range(len(string)):
        for j, ele in enumerate(string):
            if ele not in vowels and i+j < len(string):
                count_stuart += 1
            elif ele in vowels and i+j < len(string):
                count_kevin += 1
    if count_kevin < count_stuart:
        print('Stuart', count_stuart)
    elif count_stuart < count_kevin:
        print('Kevin', count_kevin)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
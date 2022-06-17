def hibaala(num_list):
    queries = int(input())
    query_list = []
    for _ in range(queries):
        query_list.append(list(map(int, input().split())))
    for i in range(queries):
        count = 0
        for ele in num_list[query_list[i][0]-1:query_list[i][1]]:
            if ele ^ query_list[i][2] > ele & query_list[i][2]:
                count += 1
        print(count)


tests = int(input())
for _ in range(tests):
    size = int(input())
    hibaala(list(map(int, input().split())))

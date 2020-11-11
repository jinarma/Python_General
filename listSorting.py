someList = ['dodo', 'john', 'jinu', 'cat', 'fish', 'elephant']
someNumList = [32, 12, 53, 2, 48, 14]
print("Unsorted: "+str(someNumList))
someNumList.sort()
print("Sorted: "+str(someNumList))
someNumList.sort(reverse=True)
print("Sorted (Reverse): "+str(someNumList))
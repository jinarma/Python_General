import os
file = open('D:/Programming/Python/Github/Python_General/BlockChainPractice/before_dawn_by_bisbiswas_dedtbrc.jpg', 'r')
print(os.stat(file.name).st_size)
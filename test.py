
matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

for index,row in enumerate(matrix):
    print(' | '.join(row))
    if (index+1) < len(matrix):
        print("---------")

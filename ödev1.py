def chess () :
    r = int(input("enter number of rows : "))
    c = int(input("enter number of columns : "))
    matrix = []

    for i in range(r) :
        a = []
        b = []
        for j in range(c):
            a.append(" O ")
            b.append(" H ")
            a.append(" H ")
            b.append(" O ")
        matrix.append(a)
        matrix.append(b)
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end="")
        print()
    
chess()
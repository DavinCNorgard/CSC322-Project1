import sys

# Extended Encoding
if __name__ == '__main__':

    def var(row, column, value):
        return 81*(row-1)+9*(column-1)+(value-1)+1

    # Read sudoku and add the given clues as clauses
    fileName = sys.argv[1]
    clauses = []
    digits = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    count = 0
    with open(fileName, "r") as f:
        row = 0
        column = 0
        while 1:
            char = f.read(1)   
            if not char:
                break
            if char in digits.keys():
                clauses.append([var(row+1, column+1, int(char))])
            if not char.isspace() or '\n' not in char:
                count = count + 1
                column = column + 1
            if count == 9:
                row = row + 1
                column = 0
                count = 0
    
    # Every cell contains at least one number
    for row in range(1, 10):
        for column in range(1, 10):
            clauses.append([var(row, column, value) for value in range(1, 10)])

    # Each number appears at most once in every row
    for i in range(1, 10):
        for k in range(1, 10):
            for j in range(1, 9):
                for l in range(j+1, 10):
                    clauses.append([-var(i, j, k), -var(i, l, k)])

    # Each number appears at most once in every column
    for j in range(1, 10):
        for k in range(1, 10):
            for i in range(1, 9):
                for l in range(i+1, 10):
                    clauses.append([-var(i, j, k), -var(l, j, k)])

    # Each number appears at most one in every 3x3 sub-grid
    for k in range(1, 10):
        for a in range(0, 3):
            for b in range(0, 3):
                for u in range(1, 4):
                    for v in range(1, 3):
                        for w in range(v+1, 4):
                            clauses.append([-var(3*a+u,3*b+v,k), -var(3*a+u,3*b+w,k)])
                for u in range(1, 3):
                    for v in range(1, 4):
                        for w in range(u+1, 4):
                            for t in range(1, 4):
                                clauses.append([-var(3*a+u,3*b+v,k), -var(3*a+w,3*b+t, k)])

    # There is at most one number in each cell (efficient encoding)
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 9):
                for l in range(k+1, 10):
                    clauses.append([-var(i, j, k), -var(i, j, l)])

    # Every number appears at least once in each row
    for i in range(1, 10):
        for k in range(1, 10):
            clauses.append([var(i, j, k) for j in range(1, 10)])

    # Every number appears at least once in each column
    for j in range(1, 10):
        for k in range(1, 10):
            clauses.append([var(i, j, k) for i in range(1, 10)])

    # Every number appears at least once in each subgrid
    for k in range(1, 10):
        for a in range(0, 3):
            for b in range(0, 3):
                clauses.append([var(3*a+u, 3*b+v, k) for u in range(1, 4) for v in range(1, 4)])

    # Create the CNF file for minisat
    f = open("puzzle.cnf", "w+")

    # Print the header line
    f.write("p cnf %d %d\n" % (729, len(clauses)))

    # Print the clauses
    for c in clauses:
        f.write(" ".join([str(l) for l in c])+" 0\n")

    # Close file created
    f.close()
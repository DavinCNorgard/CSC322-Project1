import sys

if __name__ == '__main__':

    def getNumber(n):
        return (n-1)%9+1

    fileName = sys.argv[1]
    number = []
    with open(fileName, 'r') as f:
        for line in f:
            if 'UNSAT' in line:
                open('solution.txt', 'w').close()
                f = open('solution.txt', 'w')
                f.write("The sudoku given is unsatisfiable.\n")
                f.close()
                break
            else:
                number.append(line.split(" "))

    if len(number) > 0:
        solution = []
        for i in range(len(number[1])):
            if int(number[1][i]) > 0:
                numberToPrint = getNumber(int(number[1][i]))
                solution.append(numberToPrint)

        f = open("solution.txt", "w+")

        for i in range(len(solution)):
            if i != 0 and i % 9 == 0:
                f.write("\n")
            if i % 9 != 0 and i % 3 == 0:
                f.write(" ")
            f.write("%d"% (solution[i]))

        f.write("\n")
        f.close()
    else:
        print("The sudoku given is unsatisfiable.")

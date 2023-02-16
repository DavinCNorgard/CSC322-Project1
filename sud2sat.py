import sys


def getNumber(n):
    return (n-1)%9+1

def main(input_file: str): 
    with open(input_file, 'r') as f:
        number, unsolvable = [], False
        cntxt = f.read()
        if "UNSAT" in cntxt:
            unsolvable = True
        else:
            number = [line.split(" ") for line in cntxt.split("\n")]
    
    if not number or unsolvable:
        open('solution.txt', 'w').close()
        with open('solution.txt', 'w') as f:
            f.write("The sudoku given is unsatisfiable.\n")
        print("The sudoku given is unsatisfiable.")
        return

    solution = []
    for i in range(len(number[1])):
        if int(number[1][i]) > 0:
            numberToPrint = getNumber(int(number[1][i]))
            solution.append(numberToPrint)

    with open("solution.txt", "w+") as f:
        for i in range(len(solution)):
            if i != 0 and i % 9 == 0:
                f.write("\n")
            if i % 9 != 0 and i % 3 == 0:
                f.write(" ")
            f.write("%d"% (solution[i]))

        f.write("\n")
    
if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)



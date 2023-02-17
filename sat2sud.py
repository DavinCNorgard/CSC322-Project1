#! /usr/bin/env python3
import sys


def main(file_name):
    number = []
    with open(file_name, 'r') as f:
        context = f.read()
        number, unsolvable = [], False
        if 'UNSAT' in context:
            unsolvable = True
        else:
            number = [l.split(" ") for l in context.split("\n")]

    if not number or unsolvable:    
        with open('solution.txt', 'w+') as f:
            f.write("The sudoku given is unsatisfiable.\n")
        print("The sudoko is unsolvable")
        return

    solution = []
    for n in number[1]:
        if int(n) > 0:
            num_to_print = (int(n) - 1) % 9 + 1
            solution.append(num_to_print)

    with open("solution.txt", "w+") as f:
        for i in range(len(solution)):
            if i != 0 and i % 9 == 0:
                f.write("\n")
            if i % 9 != 0 and i % 3 == 0:
                f.write(" ")
            f.write("%d"% (solution[i]))
        f.write("\n")

if __name__ == '__main__':
    file_name = sys.argv[1]
    main(file_name)

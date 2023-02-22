#! /usr/bin/env python3
import sys
from sud2sat import Sud2Sat
import sud2sat


def main(sudo_file):
    sudoku = Sud2Sat(sudo_file, True)
    sudokuRules = sud2sat.get_sudoku_rules() 
    clueClauses = sudoku._get_clues_clauses()
    clauses = sudokuRules + clueClauses

    # There is at most one number in each cell (efficient encoding)
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 9):
                for l in range(k+1, 10):
                    clauses.append([-sudoku.var(i, j, k), -sudoku.var(i, j, l)])

    # Every number appears at least once in each row
    for i in range(1, 10):
        for k in range(1, 10):
            clauses.append([sudoku.var(i, j, k) for j in range(1, 10)])

    # Every number appears at least once in each column
    for j in range(1, 10):
        for k in range(1, 10):
            clauses.append([sudoku.var(i, j, k) for i in range(1, 10)])

    # Every number appears at least once in each subgrid
    for k in range(1, 10):
        for a in range(0, 3):
            for b in range(0, 3):
                clauses.append([sudoku.var(3*a+u, 3*b+v, k) for u in range(1, 4) for v in range(1, 4)])

    with open("puzzle.cnf", "w+") as f:
        # Print the header line
        f.write("p cnf %d %d\n" % (729, len(clauses)))

        # Print the clauses
        for c in clauses:
            f.write(" ".join([str(l) for l in c])+" 0\n")

if __name__ == '__main__':
    sudo_file = sys.argv[1]
    main(sudo_file)

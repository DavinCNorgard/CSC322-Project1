#! /usr/bin/env python3
import sys
from sud2sat import Sud2Sat
import sud2sat


def main(sudo_file):
    # Efficient Encoding
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

    with open("puzzle.cnf", "w+") as f:
        # Print the header line
        f.write("p cnf %d %d\n" % (729, len(clauses)))

        # Print the clauses
        for c in clauses:
            f.write(" ".join([str(l) for l in c])+" 0\n")

if __name__ == '__main__':
    sudo_file = sys.argv[1]
    main(sudo_file)

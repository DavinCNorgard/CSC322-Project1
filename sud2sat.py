#! /usr/bin/env python3
import sys
import re

def var(row, column, value)->int:
    # this function return a representation of specific value in specific row and column
    return 81*(row-1)+9*(column-1)+(value-1)+1

def _get_rows_cols_clauses():
    # Each number appears at most once in every row and every column
    clauses = []
    for i in range(1, 10):
        for k in range(1, 10):
            for j in range(1, 9):
                for l in range(j+1, 10):
                    clauses.append([-var(i, j, k), -var(i, l, k)]) #rows
                    clauses.append([-var(j, i, k), -var(l, i, k)]) #columns
    return clauses

def _get_boxes_clauses():
    # Each number appears at most one in every 3x3 sub-grid
    clauses = []
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
    return clauses

def get_sudoku_rules():
    clauses = []
    # Every cell contains at least one number
    for row in range(1, 10):
        for column in range(1, 10):
            clauses.append([var(row, column, value) for value in range(1, 10)])
    
    clauses += _get_rows_cols_clauses()
    clauses += _get_boxes_clauses()

    return clauses

class Sud2Sat():
    def var(self, row, column, value)->int:
        # this function return a representation of specific value in specific row and column
        return 81*(row-1)+9*(column-1)+(value-1)+1

    def __init__(self, file_str : str, isFile: bool) -> None:
        if(isFile):
            #file input
            with open(file_str, "r") as f:
                self.sudoku = re.sub(r"[\n\t\s]*", "", f.read()) #remove spaces, tabs and new lines
        else:
            #string input
            self.sudoku = file_str
            

    def _get_clues_clauses(self) -> list:
        # Read sudoku and add the given clues as clauses
        clauses = []
        for row in range(9):
            for col in range(9):
                curr_char = self.sudoku[row*9 + col]
                if curr_char.isnumeric() and int(curr_char): # if number and not zero
                    clauses.append([self.var(row+1, col+1, int(curr_char))])
        return clauses


def main(sudo_file):
    sudoku = Sud2Sat(sudo_file, True)
    sudokuRules = get_sudoku_rules() 
    clueClauses = sudoku._get_clues_clauses()
    clauses = sudokuRules + clueClauses

    with open("puzzle.cnf", "w+") as f:
        # Print the header line
        f.write("p cnf %d %d\n" % (729, len(clauses)))

        # Print the clauses
        for c in clauses:
            f.write(" ".join([str(l) for l in c])+" 0\n")

if __name__ == '__main__':
    sudo_file = sys.argv[1]
    main(sudo_file)

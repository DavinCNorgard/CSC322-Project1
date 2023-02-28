#! /usr/bin/env python3
import sys
from sud2sat import Sud2Sat
import sud2sat


def main(top95File):

    #only get the rules once to improve preformance
    sudokuRules = sud2sat.get_sudoku_rules()
    Lines = []
    count = 1

    #get each line (puzzle) form the 95 puzzles list
    with open(top95File, "r") as top95:
        Lines = top95.readlines()


    for line in Lines:
        
        #go through and create cnf's
        sudoku = Sud2Sat(line, False)
        clueClauses = sudoku._get_clues_clauses()
        clauses = sudokuRules + clueClauses

        #write correct clauses to each cnf file
        with open("ExtendedTask1Storage/cnfs/"+str(count)+".cnf", "w+") as f:
            # write the header line
            f.write("p cnf %d %d\n" % (729, len(clauses)))

            # write the clauses
            for c in clauses:
                f.write(" ".join([str(l) for l in c])+" 0\n")\


        count+=1

if __name__ == '__main__':
    top95File = sys.argv[1]
    main(top95File)

#! /usr/bin/env python3
import sys
import os
    

def main():
    count=1

    while(count<=95):

        #call minisat, with the count
        os.system("minisat ExtendedTask1Storage/cnfs/"+str(count)+".cnf ExtendedTask1Storage/assigns/"+str(count)+".txt > ExtendedTask1Storage/stats/"+str(count)+".txt")

        count+=1
    
    #reset the count
    count=1

    #open solutions file for writing
    with open('solutions95.txt', 'w+') as fOut:

        while(count<=95):
            
            number = []
            #open each assign file that minisat has generated and get solution
            with open("ExtendedTask1Storage/assigns/"+str(count)+".txt", 'r') as fIn:
                context = fIn.read()
                number, unsolvable = [], False
                if 'UNSAT' in context:
                    unsolvable = True
                else:
                    number = [l.split(" ") for l in context.split("\n")]

            if not number or unsolvable:    
                #this puzzle is unsolveable
                fOut.write("The sudoku given is unsatisfiable.\n")
                print("The sudoku is unsolvable")
            else:
                #this puzzle has a solution
                solution = []
                for n in number[1]:
                    if int(n) > 0:
                        num_to_print = (int(n) - 1) % 9 + 1
                        solution.append(num_to_print)

                #write to solutions output file
                for i in range(len(solution)):
                    fOut.write("%d"% (solution[i]))
                fOut.write("\n")

            count+=1



if __name__ == '__main__':
    main()

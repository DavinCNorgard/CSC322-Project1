# Sudoku SAT Solver
## CSC 322 Project 1
Sudoku SAT-Solver is a solver that translates a Sudoko puzzle into CNF clauses and produces a solution using minisat.
    
## Authors
- Ahmed Mahmoud [V00936871]
- Davin Norgard [V00929845]
- Rastin Rashidi [V00963407]
-

## Getting Started
### Setup the files
Copy and paste the following commands to allow using `.\file` instead of `.\file.py`
```
ln -s sud2sat.py sud2sat
ln -s sud2sat1.py sud2sat1
ln -s sud2sat2.py sud2sat2
ln -s sud2sat3.py sud2sat3
ln -s sat2sud.py sat2sud
ln -s sat2sud1.py sat2sud1
ln -s sat2sud2.py sat2sud2
ln -s sat2sud3.py sat2sud3
```
### Setup Minisat
Ensure that minisat is installed, if not found then install it using 
```sudo apt-get install -y minisat```

## Running
For solving a sudoku, a sudoku should be inputed in a text file with 0's or dots for the unkown, and actual numbers for the knowns. Let's assume you have a `puzzle.txt` file containing the sudoku, and you are using the basic version `sud2sat` and `sat2sud`

Generating a `puzzle.cnf` file having the CNF of the inputed puzzle:
```
./sud2sat puzzle.txt >puzzle.cnf
```

Using minisat to solve the CNF generated above:
```
minisat puzzle.cnf assign.txt >stat.txt
```

Writing the SAT output into `solution.txt` file containg the solved sudoku:
```
./sat2sud assign.txt >solution.txt
```

Now you have the solved sudoko in `solution.txt`, but you can still see it in the terminal using `cat` command:
```
cat solution.txt
```

## Running extended task 1
Using extended commands for extended task 1 are sightly differnt than the basic task as it involves solving 95 sodoku puzzles instead of one.

IMPORTANT: before usage, this task requires the executable command `sud2sat`, please run `ln -s sud2sat.py sud2sat` if you have not already created the exectuble. the file `sud2sat1` relies on `sud2sat`.

Start with the text file of all 95 puzzles, in our case this is labelled `top95.txt`

Now you have to generate cnf files for each puzzle, use the `sud2sat1` command:
```
./sud2sat1 top95.txt
```

You have now generated 95 seperate cnf files, labelled `(1-95).cnf` in the `/ExtendedTask1Storage/cnfs` directory.

Now you can use the `sat2sud1` command to solve and output the corresponding information about each puzzle:
```
./sat2sud1
```

You have now solved all the sudokus, there is a `/ExtendedTask1Storage/assigns` directory containing the raw files from each puzzle after calling minisat lablled `(1-95).txt`.  Additionally the `/ExtendedTask1Storage/stats` directory holds the stat files lablled `(1-95).txt` for each puzzle. The solutions are located in the main directory in the file `solutions95.txt`, these solution will be one file line and be orded the same as the input file (`top95.txt`). 

Now you have the solved sudoko in `solutions95.txt`, but you can still see it in the terminal using `cat` command:
```
cat solutions95.txt
```

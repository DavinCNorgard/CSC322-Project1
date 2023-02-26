# Sudoku SAT Solver
## CSC 322 Project 1
Sudoku SAT-Solver is a solver that translates a Sudoko puzzle into CNF clauses and produces a solution using minisat.
    
## Authors
- Ahmed Mahmoud [V00936871]
- Davin Norgard [V00929845]
- Rastin Rashidi [V00963407]
- Vladimir Doricic [V00854467]

## Getting Started
### Prerequisites
Ensure that minisat is installed. If not, install it using
```
sudo apt-get install -y minisat
```
### Setup the files
To setup the files, simply run the command
```
make
```
This will unzip the file needed for Extended Task 1 and create a symbolic link for all the Python files.
## Running the Basic Task
- Ensure that the Sudoku puzzle that will be inputed is in a text file with a 0, ., ∗ or ? for the unknowns.
- There is a sample puzzle provided called `puzzle.txt`.
- For Extended Task 1, there is a `top95.txt` file provided.
- You are welcome to edit the `puzzle.txt` file or even add your own puzzles!

### Step 1
Generating a `puzzle.cnf` file having the CNF of the inputed puzzle:
```
./sud2sat puzzle.txt >puzzle.cnf
```

### Step 2
Using minisat to solve the CNF generated above:
```
minisat puzzle.cnf assign.txt >stat.txt
```

### Step 3
Writing the SAT output into `solution.txt` file containing the solved Sudoku:
```
./sat2sud assign.txt >solution.txt
```

### Step 4
Now that you have the solved Sudoku in `solution.txt`, you can view it in the terminal using `cat` command:
```
cat solution.txt
```

## Running Extended Task 1
- For Extended Task 1, there is a text file provided called `top95.txt` which contains the top95 Sudoku puzzles. There are 95 lines and each line is a Sudoku puzzle.
- For Extended Task 2 and 3, ensure that the Sudoku puzzle that will be inputed is in a text file with a 0, ., ∗ or ? for unknowns. We have provided a sample file called `puzzle.txt` but you are welcome to edit this or to add your own puzzle!
- Ensure that you have ran the `make` command, which unzips the ExtendedTask1Storage.zip.

### Extended Task 1
Now you have to generate cnf files for each puzzle, use the `sud2sat1` command:
```
./sud2sat1 top95.txt
```

You have now generated 95 seperate cnf files, labelled `(1-95).cnf` in the `/ExtendedTask1Storage/cnfs` directory.

Now you can use the `sat2sud1` command to solve and output the corresponding information about each puzzle:
```
./sat2sud1
```

You have now solved all 95 Sudoku puzzles. There is an `/ExtendedTask1Storage/assigns` directory containing the raw files from each puzzle after calling minisat labeled `(1-95).txt`.  Additionally, the `/ExtendedTask1Storage/stats` directory holds the stat files labeled `(1-95).txt` for each puzzle. The solutions are located in the main directory in the file `solutions95.txt`. The solutions will consist of 95 lines, and each line will contain the solved Sudoku corresponding to the line from the input file `top95.txt`.

Now you have the solved sudoko in `solutions95.txt`, but you can still see it in the terminal using `cat` command:
```
cat solutions95.txt
```

### Extended Task 2
Generating a `puzzle.cnf` file having the CNF of the inputed puzzle for the efficient encoding:
```
./sud2sat2 puzzle.txt >puzzle.cnf
```

Using minisat to solve the CNF generated above:
```
minisat puzzle.cnf assign.txt >stat.txt
```

Writing the SAT output into `solution.txt` file containing the solved Sudoku for the efficient encoding:
```
./sat2sud2 assign.txt >solution.txt
```

Now that you have the solved Sudoku in `solution.txt`, you can view it in the terminal using `cat` command:
```
cat solution.txt
```

### Extended Task 3
Generating a `puzzle.cnf` file having the CNF of the inputed puzzle for the extended encoding:
```
./sud2sat3 puzzle.txt >puzzle.cnf
```

Using minisat to solve the CNF generated above:
```
minisat puzzle.cnf assign.txt >stat.txt
```

Writing the SAT output into `solution.txt` file containing the solved Sudoku for the extended encoding:
```
./sat2sud3 assign.txt >solution.txt
```

Now that you have the solved Sudoku in `solution.txt`, you can view it in the terminal using `cat` command:
```
cat solution.txt
```

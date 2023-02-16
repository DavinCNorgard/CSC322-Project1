# Suduko SAT Solver
## CSC 322, Proj 1
Sudoko Sat Solver is a solver that trasnfer sudoko into a CNF formula and then solve it using minisat
    
## Authors
- Ahmed Mahmoud [V00936871]
- 
-
-

## Getting Started
### Setup the files
Copy and paste the following commands to allow using `.\file` instead of `.\file.py`
```
ln -s sud2sat.py sud2sat
ln -s sud2sat2.py sud2sat2
ln -s sud2sat3.py sud2sat3
ln -s sat2sud.py sat2sud
ln -s sat2sud2.py sat2sud2
ln -s sat2sud3.py sat2sud3
```
### Setup Minisat
Ensure that minisat is installed, if not found then install it using 
```sudo apt-get install -y minisat```

## Runing
For solving a sudoko, a sudoko should be inputed in a text file with 0's or dots for the unkown, and actual numbers for the knowns. Let's assume you have a `puzzle.txt` file containing the sudoko, and you are using the basic version `sud2sat` and `sat2sud`

Generating a `puzzle.cnf` file having the CNF of the inputed puzzle:
```
./sud2sat puzzle.txt >puzzle.cnf
```

Using minisat to solve the CNF generated above:
```
minisat puzzle.cnf assign.txt >stat.txt
```

Writing the SAT output into `solution.txt` file containg the solved sudoko:
```
./sat2sud assign.txt >solution.txt
```

Now you have the solved sudoko in `solution.txt`, but you can still see it in the terminal using `cat` command:
```
cat solution.txt
```

all: sud2sat sud2sat1 sud2sat2 sud2sat3 sat2sud sat2sud1 sat2sud2 sat2sud3 unzip

sud2sat:
	ln -s sud2sat.py sud2sat
sud2sat1:
	ln -s sud2sat1.py sud2sat1
sud2sat2:
	ln -s sud2sat2.py sud2sat2
sud2sat3:
	ln -s sud2sat3.py sud2sat3
sat2sud:
	ln -s sat2sud.py sat2sud
sat2sud1:
	ln -s sat2sud1.py sat2sud1
sat2sud2:
	ln -s sat2sud2.py sat2sud2
sat2sud3:
	ln -s sat2sud3.py sat2sud3
unzip:
	unzip ExtendedTask1Storage.zip

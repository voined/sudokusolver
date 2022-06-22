import numpy as np

sudoku = [[8,3,0, 0,5,0, 0,0,0], #0
		  [0,0,0, 7,3,4, 6,0,0], #1
		  [0,0,0, 0,2,1, 0,4,9], #2

		  [0,0,0, 0,9,0, 4,8,0], #3
		  [0,0,0, 0,0,0, 0,3,0], #4
		  [0,7,6, 0,1,0, 9,2,0], #5

		  [3,1,0, 0,0,0, 2,0,0], #6
		  [0,0,9, 0,0,0, 0,0,3], #7
		  [0,0,0, 0,0,0, 0,0,0]] #8
#          0 1 2  3 4 5  6 7 8



def box_check(y, x, value):
	for i in range(9):
		if sudoku[y][i] == value or sudoku[i][x] == value:
			return False

	for i in range(3): #y
		for j in range(3): #x
			i1 = i + y//3 * 3
			j1 = j + x//3 * 3

			if sudoku[i1][j1] == value:
				return False

	return True




solution = 1
def solve():
	global sudoku
	global solution
	for i in range(9): #y
		for j in range(9): #x
			if sudoku[i][j] == 0:
				for k in range(1, 10):
					if box_check(i, j, k):
						sudoku[i][j] = k
						solve()
						sudoku[i][j] = 0

				return

	
	print('Solution #' + str(solution))
	print(np.matrix(sudoku))
	print()
	solution += 1







solve()





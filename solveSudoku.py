'''
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0

3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9
'''
import copy

def main():
	sudoku = [	[0, 0, 0, 0, 0, 0, 0, 6, 3],
				[0, 3, 0, 0, 0, 0, 0, 5, 0],
			  	[0, 0, 0, 0, 3, 5, 0, 0, 0],
			   	[0, 0, 0, 0, 0, 0, 0, 0, 0],
			  	[0, 5, 3, 8, 0, 0, 0, 0, 0],
			   	[0, 0, 0, 5, 0, 0, 3, 0, 1],
			  	[0, 0, 0, 2, 5, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 7, 0],
			  	[0, 4, 2, 0, 1, 0, 0, 0, 0]]

	printSudoku(sudoku)
	sudoku = ultimateSudokuSolver(sudoku)
	
	if sudoku:
		printSudoku(sudoku)


def ultimateSudokuSolver(sudoku):
	# trying to solve without any guesses
	sudoku = solveSudoku(sudoku)
	if isFinished(sudoku) and isSolved(sudoku):
			return(sudoku)
	else:
		key , values = getBestGuess(getPossibilities(sudoku))
		for i in values:
			guessedSudoku = copy.deepcopy(sudoku)
			guessedSudoku[int(key) // 10][int(key) % 10] = i
			print("Guessing",i,"at",key,"Out of all possiblities:",values)
			guessedSudoku = ultimateSudokuSolver(guessedSudoku)
			if guessedSudoku != False:
				return guessedSudoku
			print("Guess",i,"at",key,"Failed! LOL")
		return False	


def getBestGuess(possiblityDict):
	currMin = 100
	minKey = 100
	minValues = []
	for key in list(possiblityDict):
		if len(possiblityDict.get(key)) < int(minKey):
			minKey = key
			minValues = possiblityDict.get(key)
	return minKey, minValues

def getPossibilities(sudoku):
	possiblityDict = {}
	for rowIndex in range(0, 9):
			for colIndex in range(0, 9):
				for num in range(1, 10):
					if safeNumRow(sudoku, num, rowIndex,
								  colIndex) and safeNumColumn(
									  sudoku, num, rowIndex,
									  colIndex) and safeNumBox(
										  sudoku, num, rowIndex, colIndex
									  ) and sudoku[rowIndex][colIndex] == 0:
						key = str(rowIndex) + str(colIndex)
						if possiblityDict.get(key):
							possiblityDict[key].append(num)
						else:
							possiblityDict[key] = [num]
	return possiblityDict

def solveSudoku(sudoku):
	iteration = 0
	change = True
	while change:
		iteration += 1
		change = False

		possiblityDict = getPossibilities(sudoku)
		
		for key in list(possiblityDict):
			if len(possiblityDict.get(key)) == 1:
				print("Inserting",possiblityDict.get(key)[0], "at",int(key) // 10,int(key) % 10)
				sudoku[int(key) // 10][int(key) % 10] = possiblityDict.get(key)[0]
				del possiblityDict[key]
				change = True
		print(
			"----------------------- Iteration",
			iteration,
			"Change",
			change,
			"--------------------",
		)
	return sudoku


def safeNumColumn(sudoku, num, rowIndex, colIndex):
	for i in range(9):
		if sudoku[i][colIndex] == num and i != rowIndex:
			return False
	return True


def safeNumRow(sudoku, num, rowIndex, colIndex):
	for i in range(9):
		if sudoku[rowIndex][i] == num and i != colIndex:
			return False
	return True


def safeNumBox(sudoku, num, rowIndex, colIndex):
	boxRowIndexStart = ((rowIndex // 3) * 3)
	boxRowIndexEnd = (((rowIndex // 3) + 1) * 3) - 1
	boxColIndexStart = ((colIndex // 3) * 3)
	boxColIndexEnd = (((colIndex // 3) + 1) * 3) - 1
	for r in range(boxRowIndexStart, boxRowIndexEnd + 1):
		for c in range(boxColIndexStart, boxColIndexEnd + 1):
			if r != rowIndex and c != colIndex:
				if sudoku[r][c] == num:
					return False
	return True


def isSolved(sudoku):
	for rowIndex in range(9):
		for colIndex in range(9):
			num = sudoku[rowIndex][colIndex]
			if not safeNumRow(sudoku, num, rowIndex, colIndex):
				return False
			if not safeNumColumn(sudoku, num, rowIndex, colIndex):
				return False
			if not safeNumBox(sudoku, num, rowIndex, colIndex):
				return False
	return True


def isFinished(sudoku):
	for rowIndex in range(9):
		for colIndex in range(9):
			if sudoku[rowIndex][colIndex] == 0:
				return False
	return True


def printSudoku(sudoku):
	for row in sudoku:
		print(' '.join(map(str, row)))


if __name__ == '__main__':
	main()

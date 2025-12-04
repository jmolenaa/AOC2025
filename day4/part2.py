from utils import *
import sys


def checkPos(pos, grid):
	if inBounds(grid, pos) and gridChar(grid, pos) == '@':
		return 1
	return 0



def checkAround(i, j, grid):
	amountOfPaper = 0
	amountOfPaper += checkPos([i + 1, j + 1], grid)
	amountOfPaper += checkPos([i + 1, j], grid)
	amountOfPaper += checkPos([i + 1, j - 1], grid)
	amountOfPaper += checkPos([i, j + 1], grid)
	amountOfPaper += checkPos([i, j - 1], grid)
	amountOfPaper += checkPos([i - 1, j + 1], grid)
	amountOfPaper += checkPos([i - 1, j], grid)
	amountOfPaper += checkPos([i - 1, j - 1], grid)
	return amountOfPaper


def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	grid = newGrid(lines)
	part1 = 0
	part2 = 0
	firstRun = True
	while True:
		removedPaper = 0
		for i, line in enumerate(grid):
			for j, char in enumerate(line):
				if char == '@':
					amountOfPaper = checkAround(i, j, grid)
					if amountOfPaper < 4:
						setGridChar(grid, [i, j], 'x')
						removedPaper += 1

		if removedPaper == 0:
			break
		part2 += removedPaper


	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])

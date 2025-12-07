from collections import defaultdict

from utils import *
import sys


def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	part1 = 0
	grid = newGrid(lines)
	startX = grid[0].index("S")
	grid[1][startX] = "|"

	for y, line in enumerate(grid[:-1]):
		splitters = [x for x, v in enumerate(line) if v == "^"]
		for splitter in splitters:
			if grid[y - 1][splitter] == "|":
				part1 += 1
				grid[y][splitter - 1] = "|"
				grid[y][splitter + 1] = "|"

		beams = [x for x, v in enumerate(line) if v == "|"]
		for beam in beams:
			if grid[y + 1][beam] == '.':
				grid[y + 1][beam] = "|"

	# part2
	grid = newGrid(lines)
	beamPos = {startX: 1}
	for y in range(2, len(grid)):
		newPos = defaultdict(int)
		for pos in beamPos:
			if grid[y][pos] == '.':
				newPos[pos] += beamPos[pos]
			if grid[y][pos] == '^':
				newPos[pos - 1] += beamPos[pos]
				newPos[pos + 1] += beamPos[pos]
		beamPos = newPos

	part2 = sum(beamPos.values())

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])

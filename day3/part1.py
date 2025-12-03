from utils import *
import sys


def findJoltage(line, lookupStart, minimumLeft):
	numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
	for number in reversed(range(10)):
		spot = line.find(str(number))
		while spot != -1 and spot <= first_spot:
			spot = line.find(str(number), spot + 1)
		if spot != -1:
			second_digit = number
			break


def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	for line in lines:
		numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]

		for number in numbers:
			spot = line.find(str(number))
			if spot != -1 and spot != len(line) - 1:
				first_digit = number
				first_spot = spot
				break
		for i in range(12):

		part1 += first_digit * 10 + second_digit
	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])

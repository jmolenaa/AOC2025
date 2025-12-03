from utils import *
import sys

def findJoltage(line, lookupStart, minimumLeft):
	for number in reversed(range(10)):
		spot = line.find(str(number), lookupStart + 1)
		if spot != -1 and spot < len(line) - minimumLeft:
			return number, spot


def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0

	for line in lines:
		next_spot = -1
		for i in reversed(range(2)):
			next_digit, next_spot = findJoltage(line, next_spot, i)
			part1 += next_digit * pow(10, i)

	for line in lines:
		next_spot = -1
		for i in reversed(range(12)):
			next_digit, next_spot = findJoltage(line, next_spot, i)
			part2 += next_digit * pow(10, i)



		# print(first_digit * 10 + second_digit)
		# part1 += first_digit * 10 + second_digit
	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])

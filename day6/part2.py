from utils import *
import sys


def addNumbers(numbers):
	result = 0
	for number in numbers:
		result += number
	return result


def multiplyNumbers(numbers):
	result = 1
	for number in numbers:
		result *= number
	return result


def tansformNumbers(numberLines):
	numberCollumns = []
	for i in range(len(numberLines[0])):
		numberCollumns.append([])
		for j in range(len(numberLines)):
			numberCollumns[i].append(numberLines[j][i])
	return numberCollumns


def transformCollumnNumbers(numbers):
	newNumbers = []
	digitsOfNumbers = [[],[],[],[]]
	for number in numbers:
		digitsOfNumbers[0].append(number % 10)
		digitsOfNumbers[1].append((number // 10) % 10)
		digitsOfNumbers[2].append((number // 100) % 10)
		digitsOfNumbers[3].append((number // 1000) % 10)

	for digits in digitsOfNumbers:
		digits = removeOccurences(digits, 0)
		# print(digits)

		newNumber = 0
		for i in range(len(digits)):
			newNumber += digits[i] * (10 ** i)
		newNumbers.append(newNumber)
	# print(digitsOfNumbers)
	print(newNumbers)
	return []


def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	signs = lines[-1].split()
	lines.remove(lines[-1])
	print(signs, lines)
	calculation = 0
	numbers = []
	calculations = []
	lenght = max(len(line) for line in lines)
	for i in range(lenght):
		number = ''.join(line[i] for line in lines if len(line) > i)
		if number.strip() == '':
			calculations.append([numbers, signs[calculation]])
			numbers = []
			# print(numbers, signs[calculation])
			# if signs[calculation] == '+':
			# 	part2 += addNumbers(numbers)
			# else:
			# 	part2 += multiplyNumbers(numbers)
			# numbers = []
			calculation += 1
		else:
			number = int(number)
			numbers.append(number)


	calculations.append((numbers, signs[-1]))
	print(calculations)
	for calculation in calculations:
		numbers = calculation[0]
		sign = calculation[1]
		if sign == '+':
			part2 += addNumbers(numbers)
		else:
			part2 += multiplyNumbers(numbers)

		# print(number)


	# for line in lines:
	# 	if line.find('*') != -1 or line.find('+') != -1:
	# 		signs = line.split()
	# 	else:
	# 		numberLines.append(getNums(line))

	# numberCollumns = tansformNumbers(numberLines)

	# for i in range(len(signs)):
	# 	numbersPart1 = numberCollumns[i]
	# 	numbersPart2 = transformCollumnNumbers(numberCollumns[i])
	#
	# 	if signs[i] == '+':
	# 		resultPart1 = addNumbers(numbersPart1)
	# 		resultPart2 = addNumbers(numbersPart2)
	# 	else:
	# 		resultPart1 = multiplyNumbers(numbersPart1)
	# 		resultPart2 = multiplyNumbers(numbersPart2)
	# 	part1 += resultPart1
	# 	part2 += resultPart2
		# print(numberCollumns[i], signs[i], "=", resultPart1 , resultPart2)

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])

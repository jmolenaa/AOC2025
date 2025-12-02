import sys


def is_repeating(string, number):
	if number * (len(string) // len(number)) == string:
		return True
	return False


def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	ranges = lines[0].split(",")
	part1 = 0
	part2 = 0
	for idRange in ranges:
		startId = int(idRange.split("-")[0])
		endId = int(idRange.split("-")[1])
		while startId != endId + 1:

			startIdString = str(startId)
			for i in range(len(startIdString) >> 1):
				number = startIdString[:i + 1]
				if is_repeating(startIdString, number):
					part2 += startId
					break


			strLength = len(startIdString)
			firstNumber = startIdString[:strLength >> 1]
			secondNumber = startIdString[strLength >> 1:]
			if firstNumber == secondNumber:
				part1 += startId

			startId += 1

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])

from utils import *
import sys


def adjustIngredientRanges(ingredientRanges):
	ingredientRanges = sorted(ingredientRanges)
	adjustedRanges = []

	for ingredientRange in ingredientRanges:
		if len(adjustedRanges) == 0 or adjustedRanges[-1][1] < ingredientRange[0]:
			adjustedRanges.append([ingredientRange[0], ingredientRange[1]])
		else:
			adjustedRanges[-1][1] = max(adjustedRanges[-1][1], ingredientRange[1])

	return adjustedRanges


def main(file):
	with open(file) as file:
		lines = file.read().split("\n\n")

	ranges = lines[0].split("\n")
	ingredients = lines[1].split("\n")


	splitUpRanges = list()
	for ingredientRange in ranges:
		splitUpRanges.append(ingredientRange.split("-"))

	for ingredientRange in splitUpRanges:
		ingredientRange[0] = int(ingredientRange[0])
		ingredientRange[1] = int(ingredientRange[1])

	part1 = 0
	part2 = 0
	for ingredient in ingredients:
		for ingredientRange in splitUpRanges:
			if int(ingredient) >= ingredientRange[0] and int(ingredient) <= ingredientRange[1]:
				part1 += 1
				break


	ingredientRanges = adjustIngredientRanges(splitUpRanges)
	for ingredientRange in ingredientRanges:
		part2 += ingredientRange[1] - ingredientRange[0] + 1


	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])

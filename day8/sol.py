from utils import *
import sys


class JunctionBox:
	def __init__(self, x: int, y: int, z: int):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return f"({self.x},{self.y},{self.z})"

	def __repr__(self):
		return f"({self.x},{self.y},{self.z})"

	def __hash__(self):
		return hash((self.x, self.y, self.z))

	def __eq__(self, other):
		if isinstance(other, JunctionBox):
			return self.x == other.x and self.y == other.y and self.z == other.z
		return False


def calculatePart1(circuits):
	part1 = 1
	circuits.sort(key=lambda c: len(c), reverse=True)
	for circuit in circuits[:3]:
		part1 *= len(circuit)
	return part1


def distanceBetweenBoxes(a: JunctionBox, b: JunctionBox):
	return (a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2


def main(file):
	with open(file) as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0
	boxes = []
	for line in lines:
		x, y, z = map(int, line.split(','))
		boxes.append(JunctionBox(x, y, z))

	distances = []
	for i, box in enumerate(boxes):
		for other_box in boxes[i + 1:]:
			distances.append((distanceBetweenBoxes(box, other_box), box, other_box))

	distances.sort(key=lambda distance: distance[0])

	circuits = []
	for i, distance in enumerate(distances):
		if i == 1001:
			part1 = calculatePart1(circuits.copy())
		box1 = distance[1]
		box2 = distance[2]
		foundCircuit = None
		newCircuits = circuits.copy()
		for circuit in circuits:
			if box1 in circuit or box2 in circuit:
				if foundCircuit is None:
					circuit.add(box1)
					circuit.add(box2)
					foundCircuit = circuit
				else:
					foundCircuit.update(circuit)
					newCircuits.remove(circuit)

		circuits = newCircuits
		if len(circuits) == 1 and len(circuits[0]) == len(boxes):
			part2 = box1.x * box2.x
			break
		if foundCircuit is None:
			circuits.append({box1, box2})

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		main("test_case")
	else:
		main(sys.argv[1])

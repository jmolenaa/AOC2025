class Point3D:
	def __init__(self, x: int, y: int, z: int):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self) -> str:
		return f"({self.x},{self.y},{self.z})"

	def __repr__(self) -> str:
		return f"({self.x},{self.y},{self.z})"

	def __hash__(self) -> int:
		return hash((self.x, self.y, self.z))

	def __eq__(self, other) -> bool:
		if isinstance(other, Point3D):
			return self.x == other.x and self.y == other.y and self.z == other.z
		return False

	def __lt__(self, other: "Point3D") -> bool:
		return (self.x, self.y, self.z) < (other.x, other.y, other.z)

	def distance_to(self, other: "Point3D") -> float:
		return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5

	def to_tuple(self) -> tuple[int, int, int]:
		return self.x, self.y, self.z


class Point2D:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

	def __str__(self) -> str:
		return f"({self.x},{self.y})"

	def __repr__(self) -> str:
		return f"({self.x},{self.y})"

	def __hash__(self) -> int:
		return hash((self.x, self.y))

	def __eq__(self, other) -> bool:
		if isinstance(other, Point2D):
			return self.x == other.x and self.y == other.y
		return False

	def __lt__(self, other: "Point2D") -> bool:
		return (self.x, self.y) < (other.x, other.y)

	def distance_to(self, other: "Point2D") -> float:
		return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

	def to_tuple(self) -> tuple[int, int]:
		return self.x, self.y
from utils import *
from point import *
import sys


def inShape(redAndGreen, point):
    directions = [Point2D(1, 0), Point2D(-1, 0), Point2D(0, 1), Point2D(0, -1)]
    for direction in directions:
        current = Point2D(point.x, point.y)
        found = False
        while minX <= current.x <= maxX and minY <= current.y <= maxY:
            if current in redAndGreen:
                found = True
                break
            current = Point2D(current.x + direction.x, current.y + direction.y)
        if not found:
            return False
    return True


def edgeInShape(redAndGreen, point1, point2):
    onEdge = False
    if point1 in redAndGreen:
        onEdge = True

    if point1.x == point2.x:
        for y in range(min(point1.y, point2.y), max(point1.y, point2.y) + 1):
            p = Point2D(point1.x, y)
            if not onEdge and p in redAndGreen:
                onEdge = True
            elif onEdge and p not in redAndGreen:
                if not inShape(redAndGreen, p):
                    return False
                onEdge = False
    elif point1.y == point2.y:
        for x in range(min(point1.x, point2.x), max(point1.x, point2.x) + 1):
            p = Point2D(x, point1.y)
            if not onEdge and p in redAndGreen:
                onEdge = True
            elif onEdge and p not in redAndGreen:
                if not inShape(redAndGreen, p):
                    return False
                onEdge = False
    return True


def main(file):
    with open(file) as file:
        lines = file.read().split("\n")

    points = []
    for line in lines:
        x, y = map(int, line.split(","))
        points.append(Point2D(x, y))

    maxArea = 0
    for i, point in enumerate(points):
        for other in points[i + 1:]:
            sidex = abs(point.x - other.x) + 1
            sidey = abs(point.y - other.y) + 1
            if sidex * sidey > maxArea:
                maxArea = sidex * sidey
    part1 = maxArea

    redAndGreen = set(points)
    for i, point in enumerate(points):
        if i == len(points) - 1:
            otherPoint = points[0]
        else:
            otherPoint = points[i + 1]

        if point.x == otherPoint.x:
            for y in range(min(point.y, otherPoint.y), max(point.y, otherPoint.y) + 1):
                p = Point2D(point.x, y)
                redAndGreen.add(p)
        elif point.y == otherPoint.y:
            for x in range(min(point.x, otherPoint.x), max(point.x, otherPoint.x) + 1):
                p = Point2D(x, point.y)
                redAndGreen.add(p)

    maxArea = 0
    print("\033[94mThese calculations are going to take a while...\033[0m")
    print("\033[94mWhenever a new max area is calculated, it will be printed below:\033[0m")
    print("\033[94mI hope you have patience :)\033[0m")
    print("\033[94mFor me the answer was calculated about halfway in, at point 218\n\n\033[0m")
    global maxX, maxY, minX, minY
    maxX = max(p.x for p in points)
    maxY = max(p.y for p in points)
    minX = min(p.x for p in points)
    minY = min(p.y for p in points)
    for i, point in enumerate(points):
        print("At point:", i, "/", len(points), ". Current max area: ", maxArea)
        for other in points[i + 1:]:
            sidex = abs(point.x - other.x) + 1
            sidey = abs(point.y - other.y) + 1
            if sidex * sidey > maxArea:
                oppositex = Point2D(point.x, other.y)
                oppositey = Point2D(other.x, point.y)
                if inShape(redAndGreen, oppositex) and inShape(redAndGreen, oppositey)\
                        and edgeInShape(redAndGreen, oppositex, point) \
                        and edgeInShape(redAndGreen, oppositey, point) \
                        and edgeInShape(redAndGreen, oppositex, other) \
                        and edgeInShape(redAndGreen, oppositey, other):
                    maxArea = sidex * sidey
                    print("\033[92mNew max area, for points: ", point, other, " Area: ", maxArea, "\033[0m")


    part2 = maxArea
    print(f"The answer to part 1 is: {part1}")
    print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main("test_case")
    else:
        main(sys.argv[1])

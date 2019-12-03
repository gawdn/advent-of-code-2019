from sys import argv


class Coordinate:
    """
    Represents a simple 2D coordinate
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_x(self, x):
        self.x += x

    def add_y(self, y):
        self.y += y

    def replace(self, c):
        """
        Replaces x, y with a new coordinate
        """
        self.x = c.x
        self.y = c.y

    def get_line_to(self, c):
        """
        Gets a list of every whole number coordinate from self to c
        """
        line = []

        x_step = 1
        y_step = 1

        if self.x > c.x:
            x_step = -1

        if self.y > c.y:
            y_step = - 1

        # Since there are no diagonals one of these loops only runs once
        for x in range(self.x, c.x + x_step, x_step):
            for y in range(self.y, c.y + y_step, y_step):
                line.append((x, y))

        return line

    def __str__(self):
        return f"Coordinate({self.x}, {self.y})"


def get_path(wire, centre):
    """
    Gets a list of each coordinate given wire directions
    """
    path = []

    position = Coordinate(0, 0)
    new_position = Coordinate(0, 0)

    for run in wire:
        direction = run[0]
        distance = int(run[1:])

        # Up (+y)
        if direction == "U":
            new_position.add_y(distance)
        # Down (-y)
        elif direction == "D":
            new_position.add_y(-distance)
        # Right (+x)
        elif direction == "R":
            new_position.add_x(distance)
        # Left (-x)
        elif direction == "L":
            new_position.add_x(-distance)
        else:
            raise ValueError(f"Don't know the direction {direction}")

        line = position.get_line_to(new_position)

        # don't double count
        if path and line[0] == path[-1]:
            line.pop(0)

        path += line

        # update position
        position.replace(new_position)

    return path


def get_intersections(wire_1, wire_2, centre=(0, 0)):
    """
    Finds all intersections between the first and second wire
    ignoring the trivial intersection at (0, 0)
    """
    wire_1_path = get_path(wire_1, centre)
    wire_2_path = get_path(wire_2, centre)
    intersections = set(wire_1_path).intersection(wire_2_path)

    print(
        f"Result (coordinate, distance): {find_closest(intersections, wire_1_path, wire_2_path)}")


def find_closest(intersections, path_1, path_2, centre=(0, 0)):
    """
    Finds closest intersection based on steps
    """
    closest = None
    min_dist = None

    for intersection in intersections:
        # Don't care about trivial case
        if intersection == centre:
            continue

        distance = path_1.index(intersection) + path_2.index(intersection)
        if closest is None or distance < min_dist:
            min_dist = distance
            closest = intersection
    return closest, min_dist


if __name__ == "__main__":
    wires = []
    if len(argv) != 2:
        raise ValueError("Not enough arguments: provide the file name")

    with open(argv[1], "r") as wires_fp:
        for line in wires_fp:
            wires.append(line.strip().split(','))

    get_intersections(wires[0], wires[1])

# Open and read in files - skipping first line
p1 = open('points1.txt', 'r')
points1 = p1.readlines()[1:]

p2 = open('points2.txt', 'r')
points2 = p2.readlines()[1:]

p3 = open('points3.txt', 'r')
points3 = p3.readlines()[1:]

p4 = open('points4.txt', 'r')
points4 = p4.readlines()[1:]


# Create a list of tuples for (x, y) positions of each point & remove excess whitespace
points = []
for line in points1:    # Switch out file name here for each run of the code
    point = line.strip().split(' ')
    points.append((float(point[0]), float(point[1])))


# Create a 'Point' class to represent all 2D points
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


# Make the points in the 'points' list into actual Point class objects
point_objects = []
for i, j in points:
    point_objects.append(Point(i, j))

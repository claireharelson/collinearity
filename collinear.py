from matplotlib import pyplot as plt
import point


# Define a function to plot the points on a graph
def collinear():
    # Plot x and y coordinates as dots
    for m in point.points:
        plt.plot(m[0], m[1], 'ro')

    # Calculate slopes between sets of four points (y2 - y1 / x2 - x1)
    slopes = []
    # I know a 4 level deep for loop is not the most efficient methodology for this but hey it works!
    for i in point.points:
        for j in point.points:
            for k in point.points:
                for n in point.points:
                    # Skip any comparisons of a point to itself
                    if j == i or k == j or k == i or n == i or n == j or n == k:
                        continue
                    else:
                        try:
                            slope1 = ((j[1] - i[1]) / (j[0] - i[0]))
                            slope2 = ((k[1] - j[1]) / (k[0] - j[0]))
                            slope3 = ((n[1] - k[1]) / (n[0] - k[0]))

                            # if 4 points are collinear, draw a line between them
                            if slope1 == slope2 and slope2 == slope3:
                                plt.plot([i[0], j[0], k[0], n[0]], [i[1], j[1], k[1], n[1]])
                                slopes.append(f"Line: {i[0], i[1]}, {j[0], j[1]}, {k[0], k[1]}, {n[0], n[1]}")

                        # Exception accounts for straight vertical lines (i.e. when x2 - x1 = 0)
                        except ZeroDivisionError:
                            if i[0] == j[0] == k[0] == n[0]:
                                plt.plot([i[0], j[0], k[0], n[0]], [i[1], j[1], k[1], n[1]])
                                slopes.append(f"Line: {i[0], i[1]}, {j[0], j[1]}, {k[0], k[1]}, {n[0], n[1]}")

    # Remove repeats of lines
    for x in slopes:
        for y in slopes:
            if x == y:
                continue
            else:
                if len(x) == len(y):
                    slopes.remove(y)

    # Needs a second round for removing duplicates
    for a in slopes:
        for b in slopes:
            if a == b:
                continue
            else:
                if len(a) == len(b):
                    slopes.remove(b)

    # Print the coordinates of the lines of collinear points
    for z in slopes:
        print(z)

    # Axis can be adjusted depending on each file of points
    plt.axis([0, 5, 0, 5])

    # Display the graph
    plt.show()


if __name__ == '__main__':
    collinear()

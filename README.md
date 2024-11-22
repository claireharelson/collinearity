This project aims to find collinear points and visualize the results. 

Point.py:
  - Reads in files and parses data (points1.txt, points2.txt, points3.txt, points4.txt)
  - Creates a class to represent an individual 2D data point

Collinear.py:
  - Uses individual points to find all 4 sets of collinear points in the 2D plane.
  - Collinearity = any set of points in a 2D plane are collinear if they all have the same pair-wise slope
      i.e.: given 3 points a, b, c -- slope b/w a&b should = slope b/w b&c
  - Lines of collinear points will always be in sets of 4
  - Uses matplotlib to visualize results (points1_graph.pdf - points4_graph.pdf)

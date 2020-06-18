#Uses python3
import sys
import math

def minimum_distance(x, y):
    points = list(zip(x, y))
    points = sorted(points, key=lambda x: x[0])

    return minimum_distance_helper(points)

def minimum_distance_helper(points):
    n = len(points)
    if n <= 3:
        return minimum_distance_bruteforce(points)

    mid = n // 2

    d1 = minimum_distance_helper(points[:mid])
    d2 = minimum_distance_helper(points[mid:])
    d = min(d1, d2)

    points_strip = []
    for p in points:
        if abs(p[0]-points[mid][0]) < d:
            points_strip.append(p)
    
    d = minimum_distance_strip(points_strip, d)

    return d

def minimum_distance_bruteforce(points):
    d = float("inf")
    for i in range(len(points)-1):
        for j in range(i+1,len(points)):
                d = min(d,dist(points[i],points[j]))
    return d

def dist(x,y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def minimum_distance_strip(points_strip, d):
    points_strip = sorted(points_strip, key=lambda x: x[1])
    for i in range(len(points_strip)-1):
        j = i + 1
        while j < len(points_strip) and points_strip[j][1] - points_strip[i][1] < d:
            d = min(d,dist(points_strip[i],points_strip[j]))
            j += 1
    return d

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments = sorted(segments)
    point = segments[0].end
    for i in range(len(segments)):
        if segments[i].start > point:
            points.append(point)
            point = segments[i].end
        elif segments[i].start <= point and segments[i].end <= point:
            point = segments[i].end
    points.append(point)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

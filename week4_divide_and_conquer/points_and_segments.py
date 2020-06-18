# Uses python3
import sys
from itertools import chain

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    start_points = zip(starts, [float("-inf")] * len(starts))
    end_points = zip(ends, [float("inf")] * len(ends))
    point_points = zip(points, range(len(points)))
    
    sort_list = chain(start_points, end_points, point_points)
    sort_list = sorted(sort_list, key=lambda x: (x[0], x[1]))

    segment = 0

    for i in sort_list:
        if i[1] == float("-inf"):
            segment += 1
        elif i[1] == float("inf"):
            segment -= 1
        else:
            cnt[i[1]] = segment
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    numRefills = 0
    lastStop = 0
    curStop = 0
    stops.insert(0,0)
    stops.append(distance)
    
    while stops[lastStop] + tank < distance:
        lastStop = curStop
        while curStop < len(stops)-1 and stops[curStop+1]-stops[lastStop] <= tank:
            curStop+=1
        if curStop == lastStop:
            return -1
        if curStop < len(stops) -1:
            numRefills += 1
    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

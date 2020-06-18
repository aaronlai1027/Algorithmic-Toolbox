# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    candy = 1
    candyLeft = n
    while candyLeft >= candy:
        summands.append(candy)
        candyLeft -= candy
        candy += 1
    summands[-1] = summands[-1] + candyLeft

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

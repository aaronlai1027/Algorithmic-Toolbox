# Uses python3
import sys


def gcd_euclidean(a, b):
    if b == 0:
        return a
        
    return gcd_euclidean(b,a%b)

def lcm(a,b):
    return (a*b)//gcd_euclidean(a,b)

# def lcm_naive(a, b):
#     for l in range(max(a,b), a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#     return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))


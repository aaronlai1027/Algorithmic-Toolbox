# Uses python3
import sys

def pisano(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range (1, m*m):
            c = (a+b) % m
            a = b
            b = c
            if (a==0 and b==1):
                return i

def get_huge_fib(n, m):
    remainder = n % pisano(m)
    first = 0
    second = 1
    res = remainder
    for i in range(1, remainder):
        res = (first+second) % m
        first = second
        second = res
    return res

# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, (previous + current)%m

#     return current

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_huge_fib(n, m))

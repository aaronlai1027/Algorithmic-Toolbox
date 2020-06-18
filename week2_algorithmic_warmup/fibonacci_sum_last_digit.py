# Uses python3
import sys

def fibonacci_sum(n):
    a = get_huge_fib(n+2)-1
    if a >= 0:
        return a
    else:
        return a + 10


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

def get_huge_fib(n, m=10):
    remainder = n % pisano(m)
    first = 0
    second = 1
    res = remainder
    for i in range(1, remainder):
        res = (first+second) % m
        first = second
        second = res
    return res

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n-1):
#         previous, current = current, (previous + current)%10
#         sum = (sum + current)%10

#     return sum

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))

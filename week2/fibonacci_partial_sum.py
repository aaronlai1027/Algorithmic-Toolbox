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

def fibonacci_partial_sum(from_, to):
    a=get_huge_fib(from_+1, 10) 
    b=get_huge_fib(to+2, 10) 
    c = b-a
    if c >= 0:
    	return c
    else:
    	return c+10



# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0

#     current = 0
#     next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             sum = (sum + current)%10

#         current, next = next, current + next

#     return sum


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
# Uses python3
import sys

def optimal_sequence_dp(n):

    operations = [("*",2),("*",3),("+",1)]
    dp = [float("inf")]*(n+1)
    dp[0] = 0
    dp[1] = 0
    for i in range(2,n+1):
        for op, num in operations:
            if i >= num:
                if op == "*" and i/num == i//num:
                    dp[i] = min(dp[i],dp[i//num]+1)
                elif op == "+":
                    dp[i] = min(dp[i],dp[i-num]+1)
    res = []
    i = n
    while i > 1:
        for op, num in operations:
            if i >= num:
                if op == "*" and i/num == i//num and dp[i] == dp[i//num] + 1:
                    res.append(i)
                    i = i//num
                elif op == "+" and dp[i] == dp[i-num] + 1:
                    res.append(i)
                    i -= 1
    res.append(1)
    return reversed(res)
        




def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence_dp(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

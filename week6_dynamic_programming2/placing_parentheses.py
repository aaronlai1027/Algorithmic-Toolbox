# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    #write your code here
    def MinAndMax(i,j):
        minValue = float("inf")
        maxValue = float("-inf")
        for k in range(i,j):
            a = evalt(M[i][k],M[k+1][j],ops[k])
            b = evalt(M[i][k],m[k+1][j],ops[k])
            c = evalt(m[i][k],M[k+1][j],ops[k])
            d = evalt(m[i][k],m[k+1][j],ops[k])
            minValue = min(minValue,a,b,c,d)
            maxValue = max(maxValue,a,b,c,d)
        return minValue, maxValue

    nums = dataset[::2]
    nums = [0]+[float(n) for n in nums]
    ops = "#"+dataset[1::2]
    n = len(nums)
    m = [[float("inf")]*n for _ in range(n)]
    M = [[float("-inf")]*n for _ in range(n)]
    for i in range(1,n):
        m[i][i] = nums[i]
        M[i][i] = nums[i]
    for length in range(1,n-1):
        for i in range(1,n-length):
            j = i + length
            m[i][j], M[i][j] = MinAndMax(i,j)

    return int(M[1][n-1])



if __name__ == "__main__":
    print(get_maximum_value(input()))

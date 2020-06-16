# Uses python3
import sys

def get_change(m):
    #write your code here
    res = 0
    for i in (10,5,1):
        while m >= i:
            m -= i
            res += 1
    return res

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

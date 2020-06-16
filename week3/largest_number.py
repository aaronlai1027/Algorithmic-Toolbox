#Uses python3

import sys

def largest_number(a):
    res = ""

    while a:
        maxDigit = 0
        for i in range(len(a)):
            if larger_value(a[i],maxDigit):
                maxDigit = a[i]
                maxIdx = i
        res += str(maxDigit)
        a.pop(maxIdx)
    return res
            
    
def larger_value(x,y):
    a = str(x)
    b = str(y)
    temp = b
    b += a
    a += temp
    return int(a) > int(b)
	

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    

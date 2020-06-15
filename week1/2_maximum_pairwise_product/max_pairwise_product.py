# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max1, max2 = 0, 0
    for i in numbers:
        if i > max2:
            max2 = i
        if i > max1:
            max2 = max1
            max1 = i
    return max1*max2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

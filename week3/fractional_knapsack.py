# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    dscIdx = []

    while capacity > 0:
        idx = -1
        unitValue = 0
        for i in range(len(weights)):
            if i not in dscIdx and values[i]/weights[i] >= unitValue:
                unitValue = values[i]/weights[i]
                idx = i

        dscIdx.append(idx)
        itemWeight = min(capacity,weights[idx])
        capacity -= itemWeight
        value += itemWeight*unitValue
        
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

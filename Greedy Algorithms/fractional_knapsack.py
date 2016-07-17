# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    total_value = 0

    while len(weights) > 0:
        if capacity == 0:
            return total_value

        # get max v/w
        best_item_index = 0
        max_value_per_weight = 0.0
        for j in range(0, len(weights)):
            if values[j]/weights[j] > max_value_per_weight:
                best_item_index = j
                max_value_per_weight = values[j]/weights[j]

        weight = min(weights[best_item_index], capacity)

        total_value += weight * max_value_per_weight
        capacity -= weight
        del weights[best_item_index]
        del values[best_item_index]

    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

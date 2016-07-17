#Uses python3

import sys

def min_dot_product(a, b):
    res = 0
    while len(a) > 0:
        # res += a[i] * b[i]
        max_a = max(a)
        min_b = min(b)
        res += max_a * min_b
        a.remove(max_a)
        b.remove(min_b)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
    

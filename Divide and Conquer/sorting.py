# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    # l <= i <= j <=r
    # for item in a[l, i]: item < a[l]
    # for item in a[i+1, j]: item == a[l]
    # for item in a[j+1, r]: item > a[l]
    x = a[l]
    i = l+1
    j = l+1
    # i, j = l + 1
    for p in range(l+1, r+1):
        if a[p] < x:
            a[p], a[j] = a[j], a[p]
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        elif a[p] == x:
            a[j], a[p] = a[p], a[j]
            j += 1
    a[i-1], a[l] = a[l], a[i-1]

    return (i, j)


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1);
    # randomized_quick_sort(a, m + 1, r);
    (m, n) = partition3(a, l, r)
    randomized_quick_sort(a, l, m-1)
    randomized_quick_sort(a, n, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

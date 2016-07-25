# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    elif left + 1 == right:
        return a[left]


    #write your code here
    middle = left + (right - left)//2
    l_ele = get_majority_element(a, left, middle)
    r_ele = get_majority_element(a, middle, right)
    if l_ele == r_ele:
        return l_ele
    else:
        l_ele_frequency = -1
        if l_ele != -1:
            l_ele_frequency = get_frequency(a[left: right], l_ele)

        r_ele_frequency = -1
        if r_ele != -1:
            r_ele_frequency = get_frequency(a[left: right], r_ele)

        if l_ele_frequency > len(a[left: right])/2:
            return l_ele
        elif r_ele_frequency > len(a[left: right])/2:
            return r_ele
        else:
            return -1


def get_frequency(a, x):
    count = 0
    for item in a:
        if item == x:
            count += 1
    return count


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

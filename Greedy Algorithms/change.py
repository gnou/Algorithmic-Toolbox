# Uses python3
import sys


def get_change(m):
    changeNum = 0
    remainder = 0
    # 10
    changeNum = m//10
    remainder = m%10

    # 5
    changeNum += remainder//5
    remainder = remainder%5

    # 1
    changeNum += remainder

    return changeNum


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

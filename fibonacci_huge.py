# Uses python3
import sys

# def fast_calc_fib(n):
#     fab_list = [0, 1]
#     if n <= 1:
#         return fab_list[n]
#
#     for i in range(2, n + 1):
#         tmp = fab_list[i - 1] + fab_list[i - 2]
#         fab_list.append(tmp)
#
#     return fab_list[n]

def is_list_repeatable(input_list = []):
    if len(input_list)%2 != 0:
        return False

    for i in range(0, len(input_list)//2):
        if input_list[i] != input_list[len(input_list)//2 + i]:
            return False

    return True

def get_fibonaccihuge(n, m):

    fab_list = [0, 1]
    pattern_list = [0, 1]

    for i in range(2, n+1):
        fab_i = fab_list[i - 1] + fab_list[i - 2]
        fab_list.append(fab_i)

        remainder_i = fab_i % m
        pattern_list.append(remainder_i)

        if is_list_repeatable(pattern_list):
            break

    pattern_length = len(pattern_list)//2
    final_remainder = n%pattern_length
    return pattern_list[final_remainder]
    # return 0

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
